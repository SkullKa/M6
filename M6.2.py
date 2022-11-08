import time
from threading import Thread

def start_car(number):
	time.sleep(1)
	print(f'Car № {number} Go!')

t1 = time.time()
for i in range(5):
	start_car(i + 1)


	print("Время работы программы с последовательным запуском функции:", round(time.time() - t1, 2), "секунд")

t2 = time.time()

threads = [Thread(target = start_car, args=(i +1, )) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()
 
print("Время работы программы с параллельным запуском потоков:", round(time.time() - t2, 2), "секунд")
