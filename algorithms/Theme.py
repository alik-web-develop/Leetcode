def reverse_string(s):
    return s[::-1]

def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Пример использования:
# print(reverse_string("leetcode"))  # Выведет: "edocteel"
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Выведет: 6
# print(single_number([4,1,2,1,2]))  # Выведет: 4
# print(is_anagram("anagram", "nagaram"))  # Выведет: True
# print(is_anagram("rat", "car"))  # Выведет: False 