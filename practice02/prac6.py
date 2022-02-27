numbers = [40, 35, 27, 50, 75]


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot]
        greater = [number for number in array[1:] if number > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


result = quick_sort(numbers)
print(result)
