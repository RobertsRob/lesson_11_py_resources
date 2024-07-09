import numpy as np
import time

# Размер массива
size = 10000000  # 10 миллион элементов

# Поэлементное умножение для NumPy array
print("start NumPy")
start_time = time.time()
arr_np1 = np.full(size, 1.5)  # Создаем массив и заполняем значениями 1.5
arr_np2 = np.full(size, 2.5)  # Создаем массив и заполняем значениями 2.5
result_np = arr_np1 * arr_np2  # Поэлементное умножение
numpy_time = time.time() - start_time

print(f"Время выполнения с NumPy (создание и умножение): {numpy_time} секунд")

# Поэлементное умножение для Python list
print("start Python list")
start_time = time.time()
array1 = [1.5] * size  # Создаем список и заполняем значениями 1.5
array2 = [2.5] * size  # Создаем список и заполняем значениями 2.5
result_py = [array1[i] * array2[i] for i in range(size)]  # Поэлементное умножение
python_time = time.time() - start_time

print(f"Время выполнения с Python списком (создание и умножение): {python_time} секунд")

# Сравнение времени выполнения
print("\nСравнение времени выполнения:")
if numpy_time < python_time:
    print("NumPy быстрее чем Python list.")
    print(f"Разница в {python_time / numpy_time} раз \n")
else:
    print("Python list быстрее чем NumPy.")
    print(f"Разница в {numpy_time / python_time} раз \n")

