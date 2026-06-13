import datetime

# go through each element and swap each pair if they are out of order, go through the list until no swaps are made
def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

# quickly sort the list by recursively selecting pivot elements and putting elements less than the pivot on the left and greater than the pivot on the right
def quick_sort(lst, start, end):
    if abs(end - start) < 2:
        return None
    elif abs(end - start) == 2:
        if lst[start] > lst[start + 1]:
            lst[start], lst[start + 1] = lst[start + 1], lst[start]
        return None
    else:
        pivot_idx = (start + end) // 2
        less_than_pointer = start
        lst[pivot_idx], lst[end - 1] = lst[end - 1], lst[pivot_idx]
        for i in range(start, end - 1):
            if lst[i] < lst[end - 1]:
                lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
                less_than_pointer += 1
        lst[less_than_pointer], lst[end - 1] = lst[end - 1], lst[less_than_pointer]
        quick_sort(lst, start, less_than_pointer)
        quick_sort(lst, less_than_pointer + 1, end)
        return None

lst = [-5.05, -5.1, -10.2, -23, 5, 100, 1293, 999.99, 999.9, 1002, 23.521, 25, 21, 29]
time_before = datetime.datetime.now()
quick_sort(lst, 0, len(lst))
time_after = datetime.datetime.now()
print(lst)
print("Sorting time was:", (time_after - time_before).total_seconds())