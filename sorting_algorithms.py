# BUBBLE SORT
def bubble_sort(nums):
    # return list if it has less than 2 elements
    if len(nums) <= 1:
        return nums
        
    for n in range(len(nums) - 1):
        changed = False
        for i in range(len(nums) - 1 - n):
            if nums[i] > nums[i + 1]:
                changed = True
                handy = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = handy
        if not changed:
            return nums
    return nums


# MERGE SORT
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    # divide list
    left = nums[:middle]
    right = nums[middle:]

    # recursion
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1

    # attach remainders
    if i < len(left):
        result.extend(left[i:])
    elif j < len(right):
        result.extend(right[j:])

    return result




    
print(f"Merge sort: {merge_sort([2, 3, 1, 5, 8])}")

print(f"Bubble sort: {bubble_sort([2, 3, 1, 5, 8])}")

