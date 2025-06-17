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

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Пример использования:
# print(reverse_string("leetcode"))  # Выведет: "edocteel"
# print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Выведет: 6
# print(single_number([4,1,2,1,2]))  # Выведет: 4
# print(is_anagram("anagram", "nagaram"))  # Выведет: True
# print(is_anagram("rat", "car"))  # Выведет: False
# print(intersection([1,2,2,1], [2,2]))  # Выведет: [2]
# print(first_uniq_char("leetcode"))  # Выведет: 0
# print(first_uniq_char("loveleetcode"))  # Выведет: 2
# arr = [1,1,2]
# k = remove_duplicates(arr)
# print(arr[:k])  # Выведет: [1, 2] 