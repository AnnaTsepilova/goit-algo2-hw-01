def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи в масиві за допомогою методу "розділяй і володарюй".

    :param arr: Список чисел
    :return: Кортеж (мінімум, максимум)
    """
    # Базовий випадок: якщо масив містить лише один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # Базовий випадок: якщо масив містить два елементи
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Розділяємо масив на дві частини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднуємо результати
    return min(left_min, right_min), max(left_max, right_max)


# Приклад використання
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_min_max(arr)
print(f"Мінімум: {result[0]}, Максимум: {result[1]}")
