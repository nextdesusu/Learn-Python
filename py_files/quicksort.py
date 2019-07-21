def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    middle = []
    left = []
    right = []
    for l_item in arr:
        if l_item < pivot:
            left.append(l_item)
    for m_item in arr:
        if m_item == pivot:
            middle.append(m_item)
    for r_item in arr:
        if r_item > pivot:
            right.append(r_item)
    return quicksort(left) + middle + quicksort(right)

print(quicksort([1, 4, 6, 1, 3, 2, 10, 11, 42, 1, 3, 2, 20]))

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
