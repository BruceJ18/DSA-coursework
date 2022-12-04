# ------------- brute force sorting portion
# inefficient time complexity of O(n^2)

def bubble_sort(list_1):
    list_1 = list(list_1)

    # 4. Repeat the process n-1 times
    for _ in range(len(list_1) - 1):

        # 1. Iterate over the array (except last element)
        for i in range(len(list_1) - 1):

            # 2. Compare the number with
            if list_1[i] > list_1[i + 1]:
                # 3. Swap the two elements
                list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]

    # Return the sorted list
    return list_1


def insert_sort(list_1):
    list_1 = list(list_1)
    for i in range(len(list_1)):
        current_num  = list_1.pop(i)
        j = i-1
        while j >= 0 and list_1[j] > list_1[i]:
            j -= 1
        list_1.insert(j + 1, current_num)



# ----------- merge sort portion
def merge_sort(left_divided_portion, right_divided_portion):
    merged_sorted_list = []
    i, j = 0, 0

    while i < len(left_divided_portion) and j < len(right_divided_portion):
        if left_divided_portion[i] <= right_divided_portion[j]:
            merged_sorted_list.append(left_divided_portion[i])
            i += 1
        else:
            merged_sorted_list.append(right_divided_portion[j])
            j += 1

    left_tail = left_divided_portion[i:]
    right_tail = right_divided_portion[j:]

    return merged_sorted_list + left_tail + right_tail




def divide(list_1):
    if len(list_1) <= 1:
        return list_1

    mid = len(list_1) / 2

    left = list_1[:mid]
    right = list_1[mid:]

    left_divided, right_divided = divide(left), divide(right)

    sorted_list = merge_sort(left_divided, right_divided)

    return sorted_list


#----------------- quick sort portion



def quick_sort(unsorted_list, start=0, end=None):
    if end is None:
        unsorted_list = list(unsorted_list)
        end = len(unsorted_list) - 1

    if start < end:
        pivot = partitions(unsorted_list, start, end)
        quick_sort(unsorted_list, start, pivot - 1)
        quick_sort(unsorted_list, start, pivot + 1)

    sorted_list = unsorted_list

    return sorted_list



def partitions(list_1, start, end):
    if end is None:
        end = len(list_1) - 1

    l, r = start, end

    while r > l:
        if list_1[l] <= list_1[end]:
            l += 1
        elif list_1[r] > list_1[end]:
            r += 1
        else:
            list_1[l], list_1[r] = list_1[r], list_1[l]

    if list_1[l] > list_1[end]:
        list_1[l], list_1[end] = list_1[end], list_1[l]
        return l
    else:
        return end