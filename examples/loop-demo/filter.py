# create a new list, which only contains
# the number in the original list which greater than 20

def filter_greater_than(numbers, limit):
    result = []
    for n in numbers:
        if n > limit:
            result.append(n)

    return result


def sort_naive(numbers):
    result = list(numbers)
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                # swap
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


numbers = [12, 45, 7, 23, 56, 89, 3, 67]
result = filter_greater_than(numbers, 20)
print(result)

numbers2 = [120, 5, 7, 3, 56, 89, 3, 67]
result = filter_greater_than(numbers2, 27)
print(result)
