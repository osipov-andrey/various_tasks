from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()
children = root.getchildren()

for student_data in children:
    print('PK: ', (student_data.attrib, student_data.get('pk')))
    print('{} {} {}'.format(
        # поиск тегов на первом уровне вложенности- дети student_data.
        student_data.find('./first_name').text,
        student_data.find('./last_name').text,
        student_data.find('./age').text
    ))

# выборка всех тегов first_names из тегов person.
first_names = root.findall('./person/first_name')
# выборка всех тегов last_names из тегов person.
last_names = root.findall('./person/last_name')
# выборка всех тегов age из тегов person.
ages = root.findall('./person/age')

# собираем теги в общие группы и создаем общий словарь для каждого person.
for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

for student_data in children:
    print("PK: ", student_data.attrib)
    for child in student_data:
        print('{}: {}'.format(child.tag, child.text))
