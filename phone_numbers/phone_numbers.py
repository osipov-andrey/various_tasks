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


Пример ввода и вывода в функции test().

'''




import re
import sys

def parse(raw_phones, raw_masks):
    # step 1: collect input
    phone_regex = re.compile(r'\D')
    phones = [phone_regex.sub('', phone) for phone in raw_phones]
    masks = [mask.split(' - ', maxsplit=1) for mask in raw_masks]
    return phones, masks

def get_patterns(masks):    
    # step 2: prepare
    patterns = {}
    for mask, v in masks:
        country, operator, number = mask.split(' ')
        pattern = f'({country[1:]}){operator}({number})'.replace('X', r'\d')
        patterns[re.compile(pattern)] = v
    return patterns
        
def format_phones(phone, patterns):
    # step 3: processing
    for k, v in patterns.items():
        match = k.fullmatch(phone)
        if match:
            return f'+{match.group(1)} ({match.group(2)}) {match.group(3)} - {v}'

def test():
        
    test_phones = [
        '28-49-5-123-45-67',
        '87544456789',
        '+28 (495) 123 45 56',
        '875-(29)-123456',
        ]
                    
    test_masks = [
        '+875 (29) 1XXXXX - Atlantis MythCell',
        '+875 (44) 4XXXXX - Atlantis MobTelecom',
        '+28 (495) XXXXXXX - ElDorado GoldLine',
        ]
    test_result = []
    
    phones, masks = parse(test_phones, test_masks)
    patterns = get_patterns(masks)
    for phone in phones:
        test_result.append(format_phones(phone, patterns))
        
    
    sample_result = [
        '+28 (495) 1234567 - ElDorado GoldLine',
        '+875 (44) 456789 - Atlantis MobTelecom',
        '+28 (495) 1234556 - ElDorado GoldLine',
        '+875 (29) 123456 - Atlantis MythCell',
        ]
        
    assert test_result == sample_result
    print('Test - OK')
        
if __name__ == '__main__':
    test()
    raw_phones = [input() for _ in range(int(input()))]
    raw_masks = [input() for _ in range(int(input()))]
    phones, masks = parse(raw_phones, raw_masks)
    patterns = get_patterns(masks)
    for phone in phones:
        print(format_phones(phone, patterns))       
        
