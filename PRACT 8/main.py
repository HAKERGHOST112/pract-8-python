import random


def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]


size = int(input("Введите размер массива: "))


array = generate_random_array(size)


print("Сгенерированный массив:", array)


element_to_find = int(input("Введите элемент для поиска: "))


if element_to_find in array:
    print(f"Элемент {element_to_find} содержится в массиве.")
else:
    print(f"Элемент {element_to_find} не содержится в массиве.")
