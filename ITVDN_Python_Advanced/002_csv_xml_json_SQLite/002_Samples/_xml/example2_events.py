from lxml import etree as ET


class PersonTarget:
    """
    Порциональная обработка данных XML файла.
    """

    def __init__(self):
        # определяем дефолтные значения перед началом работы
        self.records = []
        self.current_index = None
        self.current_node = None

    def start(self, tag, attrib):
        # при входе в тег person, добавляем новую запись в список,
        # которую далее будем заполнять в методе data.
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'last_name': '',
                'age': None,
                'metadata': attrib
            })
            self.current_index = len(self.records) - 1
        # указываем текущий тег, чтобы проверять его в data.
        self.current_node = tag

    def end(self, tag):
        # по завершению теги сбрасываем текущий тег
        self.current_node = ''

    def data(self, data):
        # print('Data: {} -> "{}"'.format(self.current_node, data))
        # проверяем текущий тег, если он является одним из интересующих нас,
        # то берем данные из тега и записываем в элемент с индексом
        # self.current_index.
        if self.current_node in ['first_name', 'last_name', 'age']:
            self.records[self.current_index][self.current_node] = data

    def close(self):
        return self.records


# связь парсера с нашим классом обработчиком- target.
parser = ET.XMLParser(target=PersonTarget())
infile = 'data/test.xml'
results = ET.parse(infile, parser)

for r in results:
    print(r)
