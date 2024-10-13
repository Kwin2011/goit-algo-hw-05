import random

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        middle = (left + right) // 2

        # Якщо цільове значення більше за середнє значення, шукаємо в правій половині
        if arr[middle] < target:
            left = middle + 1

        # Якщо цільове значення менше за середнє значення, шукаємо в лівій половині
        elif arr[middle] > target:
            right = middle - 1

        # Якщо знайшли точне значення
        else:
            return steps, arr[middle]

    # Якщо не знайшли точне значення, повертаємо найближчий більший або None
    # closest = arr[left] if left < len(arr) else None
    # return steps, closest
    return None,

# Тестування
arr = [random.randint(0, 100) for _ in range(random.randint(1, 50))]
arr.sort()  # Сортуємо масив для бінарного пошуку

target = 5
result = binary_search(arr, target)
print(f"Відсортований масив: {arr}")
print(f"Результат пошуку для {target}: {result}")
