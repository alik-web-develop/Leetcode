# # # # # # # # Решение Two Sum
# # # # # # # # class TwoSum:
# # # # # # # #     def twoSum(self, nums, target):
# # # # # # # #         hash_map = {}
# # # # # # # #         for i, num in enumerate(nums):
# # # # # # # #             complement = target - num
# # # # # # # #             if complement in hash_map:
# # # # # # # #                 return [hash_map[complement], i]
# # # # # # # #             hash_map[num] = i
# # # # # # # #         return []

# # # # # # # # Решение Valid Parentheses
# # # # # # # # class ValidParentheses:
# # # # # # # #     def isValid(self, s):
# # # # # # # #             next_temp = current.next
# # # # # # # #             current.next = prev
# # # # # # # #             prev = current
# # # # # # # #             current = next_temp
# # # # # # # #         return prev

# # # # # # # # Решение Merge Two Sorted Lists
# # # # # # # #         current = dummy
# # # # # # # #             current = current.next
# # # # # # # #         current.next = l1 if l1 else l2
# # # # # # # #         return dummy.next

# # # # # # # #             if nums[mid] == target:
# # # # # # # #                 right =
# # # # # # # # Решение Climbing Stairs
# # # # # # # # class Cl``