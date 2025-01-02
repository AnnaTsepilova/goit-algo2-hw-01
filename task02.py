import random


def quick_select(arr, k):
    """
    Знаходить k-й найменший елемент у масиві за допомогою алгоритму Quick Select.

    :param arr: Список чисел
    :param k: Позиція найменшого елемента (1 <= k <= len(arr))
    :return: k-й найменший елемент
    """
    if len(arr) == 1:
        return arr[0]

    # Вибір опорного елемента (pivot) випадковим чином
    pivot = random.choice(arr)

    # Розподіл елементів навколо опорного
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    # Визначаємо позицію k відносно розмірів підмасивів
    if k <= len(smaller):
        return quick_select(smaller, k)
    elif k <= len(smaller) + len(equal):
        return pivot
    else:
        return quick_select(larger, k - len(smaller) - len(equal))


# Приклад використання
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = quick_select(arr, k)
print(f"{k}-й найменший елемент: {result}")