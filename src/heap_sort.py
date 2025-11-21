def __max_heap__(arr, n, parent_id):
    largest = parent_id
    left_child = 2 * largest + 1
    right_child = 2 * largest + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != parent_id:
        arr[parent_id], arr[largest] = arr[largest], arr[parent_id]
        __max_heap__(arr, n, largest)


def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        __max_heap__(arr, len(arr), i)

    end = len(arr)
    for i in range(end - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __max_heap__(arr, i, 0)
