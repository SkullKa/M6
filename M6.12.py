import time
from threading import Thread
from datetime import datetime

def start_car(number):
	time.sleep(1)
	print(f'Car № {number} Go!')

t1 = datetime.now()
for i in range(5):
	start_car(i + 1)


	print('Время работы программы с последовательным запуском функции:', (datetime.now() - t1).microseconds)

t2 = datetime.now()

threads = [Thread(target = start_car, args=(i +1, )) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()
 
print('Время работы программы с последовательным запуском функции:', (datetime.now() - t2).microseconds)
