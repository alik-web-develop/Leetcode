def reverse_string(s):
    return s[::-1]

def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Пример использования:
# print(reverse_string("leetcode"))  # Выведет: "edocteel"
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Выведет: 6 