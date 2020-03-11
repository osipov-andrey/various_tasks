from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

# search value
# выборка тегов first_name из тегов person с атрибутом pk = 21
first_names = root.findall('./person[@pk="21"]/first_name')
# выборка тегов last_name из тегов person с атрибутом pk = 21
last_names = root.findall('person[@pk="21"]/last_name')
# выборка тегов age из тегов person с атрибутом pk = 21
ages = root.findall('person/[@pk="21"]/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

# выборка текста у тега first_name у person с атрибутом pk и индексом 1 в DOM
last_name = root.find('./person/age/..[@pk][1]/first_name').text
print(last_name)

# выборка текста у тега first_name у person с атрибутом pk и индексом 2 в DOM
last_name = root.find('./person/age/..[@pk][2]/first_name').text
print(last_name)

# выборка текста у тега first_name у person с атрибутом pk и индексом 3 в DOM
last_name = root.find('./person/age/..[@pk][3]/first_name').text
print(last_name)
