def coroutine_hand_maid(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


@coroutine_hand_maid
def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen recived: ', message)


@coroutine_hand_maid
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('.......................')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average

# g = average()
# g.send(5)
# g.send(6)
#
# try:
#     g.throw(StopIteration)
# except StopIteration as e:
#     print('Average', e.value)
