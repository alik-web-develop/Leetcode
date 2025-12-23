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
# # # # # # # #                 right = mid - 1

# # # # # # # # Решение Climbing Stairs
# # # # # # # # class ClimbingStairs:
# # # # # # # #         if n <= 2:
# # # # # # # #             return n
# # # # # # # #         dp = [0] * (n + 1)
# # # # # # # #         dp[1] = 1
# # # # # # # #         dp[2] = 2
# # # # # # # #         for i in range(3, n + 1):
# # # # # # # #             dp[i] = dp[i-1] + dp[i-2]
# # # # # # # #         return dp[n]

# # # # # # # # Решение Valid Palindrome
# # # # # # # # class ValidPalindrome:
# # # # # # # #     def isPalindrome(self, s):
# # # # # # # #         s = ''.join(c.lower() for c in s if c.isalnum())
# # # # # # # #         return s == s[::-1]

# # # # # # # # Решение Maximum Subarray
# # # # # # # # class MaximumSubarray:
# # # # # # # #     def maxSubArray(self, nums):
# # # # # # # #         max_sum = current_sum = nums[0]
# # # # # # # #         for num in nums[1:]:
# # # # # # # #             current_sum = max(num, current_sum + num)