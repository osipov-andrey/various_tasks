'''
Задача "Телефонные номера".

Есть база данных телефонных номеров. Необходимо для каждого номера определить 
страну, оператора, а также привести номер в определённый формат. 


Формат ввода

Первая строка содержит число N (1≤N≤1000) – количество номеров в базе данных.

Далее следует N строк – номера телефонов по одному номеру в строке. 
Длина строки не превосходит 100 символов.

Следующая строка содержит число M (1≤M≤1000) – количество шаблонов.

Далее M строк – шаблоны в формате, описанном выше. Длина шаблона не п
ревосходит 100 символов.


'''





import re
import sys

# step 1: collect input
phone_regex = re.compile(r'\D')

phones = [phone_regex.sub('', input()) for _ in range(int(input()))]
masks = [input().split(' - ', maxsplit=1) for _ in range(int(input()))]

# step 2: prepare
patterns = {}
for mask, v in masks:
    country, operator, number = mask.split(' ')
    pattern = f'({country[1:]}){operator}({number})'.replace('X', r'\d')
    patterns[re.compile(pattern)] = v

# step 3: processing
for phone in phones:
    for k, v in patterns.items():
        match = k.fullmatch(phone)
        if match:
            print(f'+{match.group(1)} ({match.group(2)}) {match.group(3)} - {v}')
            break
