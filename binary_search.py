import time

# linear search of list with time complexity O(n)
def linear_count_rotaions(list):
    position = 0

    while position <= len(list):
        if list[position] < list[position-1]:
            return position
        else:
            position += 1
    return -1



# binary search of list with time complexity O(log(n))
def count_rotations(list):
    start = 0
    end = len(list)-1
    while start <= end:
        mid_index = (end+start) // 2
        mid_value = list[mid_index]
        one_less_mid = list[mid_index-1]
        end_value = list[end]
        print(f"start: {start}", f"end: {end}", f"mid_index: {mid_index}", f"mid_value: {mid_value}")
        time.sleep(3)
        # mid_index must be > 0 to validate the second conditional statement
        # 
        if mid_index > 0 and mid_value < one_less_mid:
            return mid_index
        elif mid_value < end_value:
            end = mid_index-1
        elif mid_value > end_value:
            start = mid_index +1
    return -1