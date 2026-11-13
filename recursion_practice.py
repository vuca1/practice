def rec_sum(nums):
    if len(nums) == 0:
        return 0
    if len(nums) <= 1:
        return nums[0]
    return nums[0] + rec_sum(nums[1:])


def reverse_string(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string(text[:-1])


print(f"Recursive sum: {rec_sum([2, 3, 5])}")
print(f"Reversed text: {reverse_string('3< olleH')}")