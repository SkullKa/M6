import requests
import time
from threading import Thread


def get_html(link):
    data = requests.get(link)
    print(link, len(data.text))


links = ['https://yandex.ru', 'https://www.google.ru', 'https://rambler.ru', 'https://github.com', 'https://brunoyam.com']
threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

t1 = time.time()
for i in range(5):
    print(get_html(links[i]))
print(f'Время работы программы с последовательным запуском функции: {time.time() - t1}')

t2 = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время работы программы с параллельным запуском функции: {time.time() - t2}')
