import requests

# pip install requests
# запускаем различные виды запросов, но уже с использованием
# библиотеки requests
response1 = requests.get('https://devpython.ru')
response2 = requests.put('https://devpython.ru')
response3 = requests.post('https://devpython.ru')
response4 = requests.delete('https://devpython.ru')
