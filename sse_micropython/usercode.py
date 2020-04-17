import picoweb
from machine import WDT
from rfid_utils import RFID, Buzzer, GLED, RLED
from webserver import eprint
# from config import settings
from uasyncio import sleep, sleep_ms, get_event_loop
from ucollections import namedtuple

##################     RFID-READER SETTINGS     ##################
sse_host = "10.10.0.1"
sse_port = 5000
picoweb_debug = True
message_to_client = "event: card\ndata: {}\n\n"
app = picoweb.WebApp("__name__")
wdt = WDT(timeout=30000)
buz = Buzzer()
rfid = RFID()
##################     ####################     ##################


# Exception raised by get_nowait().
class QueueEmpty(Exception):
    pass


# Exception raised by put_nowait().
class QueueFull(Exception):
    pass


class Queue:
    """ https://github.com/peterhinch/micropython-async/tree/master/v3
    /primitives """

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._queue = []

    def _get(self):
        return self._queue.pop(0)

    async def get(self):
        """Usage: item = await queue.get()"""
        while self.empty():
            # Queue is empty, put the calling Task on the waiting queue
            await sleep_ms(0)
        return self._get()

    def get_nowait(self):
        """Remove and return an item from the queue.
        Return an item if one is immediately available, else raise
        QueueEmpty."""
        if self.empty():
            raise QueueEmpty()
        return self._get()

    def _put(self, val):
        self._queue.append(val)

    async def put(self, val):
        """Usage: await queue.put(item)"""
        while self.qsize() >= self.maxsize and self.maxsize:
            # Queue full
            await sleep_ms(0)
            # Task(s) waiting to get from queue, schedule first Task
        self._put(val)

    def put_nowait(self, val):
        """ Put an item into the queue without blocking. """
        print("QUEUE SELF SIZE: {}".format(self.qsize()))
        print("QUEUE SELF ID: {}".format(id(self)))
        if self.qsize() >= self.maxsize and self.maxsize:
            raise QueueFull()
        self._put(val)

    def qsize(self):
        """Number of items in the queue."""
        return len(self._queue)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self._queue) == 0

    def full(self):
        """Return True if there are maxsize items in the queue.
        Note: if the Queue was initialized with maxsize=0 (the default),
        then full() is never True."""
        if self.maxsize <= 0:
            return False
        else:
            return self.qsize() >= self.maxsize


class AsyncIterable:
    """ Async iterator to wrap Queue """

    def __init__(self, iterable):
        self.data = iterable
        self.index = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        await sleep(0.1)
        x = await self.data.get()
        return x


class Publisher:
    """
    SSE-handler.
    Micropython version of server-sent-events library:

        https://github.com/boppreh/server-sent-events

    """

    Subscriber = namedtuple('Subscriber', ['ID', 'queue'])

    def __init__(self):
        """
        Creates a new publisher with an empty list of subscribers.
        """
        self.subscribers_by_channel = dict()

    def _get_subscribers_lists(self, channel):
        yield self.subscribers_by_channel.setdefault(channel, [])
        # списки подписчиков на канал

    def get_subscribers(self, channel='default channel'):
        for subscriber_list in self._get_subscribers_lists(channel):
            yield from subscriber_list

    def subscribe(self, channel='default channel'):

        q = Queue(15)
        subscriber = self.Subscriber(id(q), q)  # namedtuple

        for subscribers_list in self._get_subscribers_lists(channel):
            subscribers_list.append(subscriber)

        return self._make_generator(subscriber)

    def unsubscribe(self, subscriber_id, channel='default channel'):
        """ Finds subscriber by his ID end removes him from subscribers
        lists """
        for subscribers_list in self._get_subscribers_lists(channel):
            subscriber_to_remove = \
                list(filter(lambda x: x.ID == subscriber_id, subscribers_list))[0]
            subscribers_list.remove(subscriber_to_remove)

    async def _make_generator(self, subscriber):
        """:returns subscriber.ID to identification and
        AsyncIterable(subscriber.queue) to write into response"""
        return (subscriber.ID, AsyncIterable(subscriber.queue))

    def _publish_single(self, data, subscriber):
        str_data = str(data)
        for line in str_data.split('\n'):
            subscriber.queue.put_nowait('{}\n'.format(line))
        # subscriber.queue.put_nowait('\n')

    def publish(self, data, channel='default channel'):
        for subscriber in self.get_subscribers(channel):
            self._publish_single(data, subscriber)


publisher = Publisher()


@app.route("/subscribe")
async def subscribe(req, resp):
    """ Handler to work with ANT.VERTEX.TEST.CLIENT """

    await sleep(0.1)
    await picoweb.start_response(resp, content_type='text/event-stream')
    subscriber_id, subscriber_aiterator = await publisher.subscribe()

    try:
        async for data in subscriber_aiterator:
            print("DATA: ", data)

            try:
                await resp.awrite(message_to_client.format(data))
                GLED.on()
                await sleep(1)
                GLED.off()
            except OSError as err:  # Client was disconnected
                print("Responsing error: {}".format(err))

                for _ in range(3):
                    buz.beep(1000)
                    await sleep(1)

                publisher.unsubscribe(subscriber_id)
                GLED.off()

    except Exception as err:  # Unexpected error
        print(err)
        raise err
    finally:
        publisher.unsubscribe(subscriber_id)
        GLED.off()


@app.route("/hello")
async def hello(req, resp):
    """Handler to work from browser. Makes request to '/subscribe' from
    browser."""
    publisher.publish("New visit!")  # Message to already connected clients

    response = """
<html>
    <body>
        <p>Open this page in new tabs to see the real time visits.</p>
        <p>Attach a card to the reader to see CardID.</p>
        <div id="events" />
        <script>
        function insertMessage(e){
            document.getElementById('events').innerHTML += e.data + '<br>';
        }
        var eventSource = new EventSource('/subscribe');
        eventSource.addEventListener('card',  insertMessage);
        </script>
    </body>
</html>
"""

    await picoweb.start_response(resp)
    await resp.awrite(response)


async def reader():
    """ Coroutine to read RFID-cards and feed WDT """
    while 1:
        if wdt:
            wdt.feed()
        await sleep(1)
        RLED.off()
        ID = rfid.read()
        if ID:
            await eprint(ID)
            await buz.beep(50)
            RLED.on()
            publisher.publish(ID)


async def run():
    await eprint("User code started")

    loop = get_event_loop()
    loop.create_task(reader())
    loop.create_task(
        app.run(host=sse_host, port=sse_port, debug=picoweb_debug))
    loop.run_forever()
