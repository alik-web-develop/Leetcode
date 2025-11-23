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
# # # # # # # #             max_sum = max(max_sum, current_sum)
# # # # # # # #         return max_sum

# # # # # # # # Решение Single Number
# # # # # # # # class SingleNumber:
# # # # # # # #     def singleNumber(self, nums):
# # # # # # # #         result = 0
# # # # # # # #         for num in nums:
# # # # # # # #             result ^= num
# # # # # # # #         return result

# # # # # # # # Решение Move Zeroes
# # # # # # # # class MoveZeroes:
# # # # # # # #     def moveZeroes(self, nums):
# # # # # # # #         non_zero = 0
# # # # # # # #         for i in range(len(nums)):
# # # # # # # #             if nums[i] != 0:
# # # # # # # #                 nums[non_zero], nums[i] = nums[i], nums[non_zero]
# # # # # # # #                 non_zero += 1

# # # # # # # # Решение Longest Common Prefix
# # # # # # # # class LongestCommonPrefix:
# # # # # # # #     def longestCommonPrefix(self, strs):
# # # # # # # #         if not strs:
# # # # # # # #             return ""
# # # # # # # #         shortest = min(strs, key=len)
# # # # # # # #         for i, char in enumerate(shortest):
# # # # # # # #             for other in strs:
# # # # # # # #                 if other[i] != char:
# # # # # # # #                     return shortest[:i]
# # # # # # # #         return shortest

# # # # # # # # Решение Longest Palindromic Substring
# # # # # # # # class LongestPalindromicSubstring:
# # # # # # # #     def longestPalindrome(self, s):
# # # # # # # #         if not s:
# # # # # # # #             return ""
        
# # # # # # # #         start = 0
# # # # # # # #         max_length = 1
        
# # # # # # # #         def expand_around_center(left, right):
# # # # # # # #             nonlocal start, max_length
# # # # # # # #             while left >= 0 and right < len(s) and s[left] == s[right]:
# # # # # # # #                 if right - left + 1 > max_length:
# # # # # # # #                     start = left
# # # # # # # #                     max_length = right - left + 1
# # # # # # # #                 left -= 1
# # # # # # # #                 right += 1
        
# # # # # # # #         for i in range(len(s)):
# # # # # # # #             expand_around_center(i, i)  # для нечетной длины
# # # # # # # #             expand_around_center(i, i + 1)  # для четной длины
            
# # # # # # # #         return s[start:start + max_length]

# # # # # # # # Решение Merge K Sorted Lists
# # # # # # # # class MergeKSortedLists:
# # # # # # # #     def mergeKLists(self, lists):
# # # # # # # #         if not lists:
# # # # # # # #             return None
            
# # # # # # # #         import heapq
        
# # # # # # # #         # Создаем минимальную кучу
# # # # # # # #         heap = []
# # # # # # # #         for i, l in enumerate(lists):
# # # # # # # #             if l:
# # # # # # # #                 heapq.heappush(heap, (l.val, i, l))
                
# # # # # # # #         dummy = ListNode(0)
# # # # # # # #         current = dummy
        
# # # # # # # #         while heap:
# # # # # # # #             val, i, node = heapq.heappop(heap)
# # # # # # # #             current.next = node
# # # # # # # #             current = current.next
            
# # # # # # # #             if node.next:
# # # # # # # #                 heapq.heappush(heap, (node.next.val, i, node.next))
                
# # # # # # # #         return dummy.next

# # # # # # # # Решение Word Ladder
# # # # # # # # class WordLadder:
# # # # # # # #     def ladderLength(self, beginWord, endWord, wordList):
# # # # # # # #         if endWord not in wordList:
# # # # # # # #             return 0
            
# # # # # # # #         wordList = set(wordList)
# # # # # # # #         queue = [(beginWord, 1)]
# # # # # # # #         visited = {beginWord}
        
# # # # # # # #         while queue:
# # # # # # # #             word, length = queue.pop(0)
# # # # # # # #             if word == endWord:
# # # # # # # #                 return length
                
# # # # # # # #             for i in range(len(word)):
# # # # # # # #                 for c in 'abcdefghijklmnopqrstuvwxyz':
# # # # # # # #                     next_word = word[:i] + c + word[i+1:]
# # # # # # # #                     if next_word in wordList and next_word not in visited:
# # # # # # # #                         queue.append((next_word, length + 1))
# # # # # # # #                         visited.add(next_word)
                        
# # # # # # # #         return 0

# # # # # # # Решение Trapping Rain Water
# # # # # # # class TrappingRainWater:
# # # # # # #     def trap(self, height):
# # # # # # #         if not height:
# # # # # # #             return 0
# # # # # # #         left, right = 0, len(height) - 1
# # # # # # #         left_max, right_max = height[left], height[right]
# # # # # # #         water = 0
# # # # # # #         while left < right:
# # # # # # #             if left_max < right_max:
# # # # # # #                 left += 1
# # # # # # #                 left_max = max(left_max, height[left])
# # # # # # #                 water += max(0, left_max - height[left])
# # # # # # #             else:
# # # # # # #                 right -= 1
# # # # # # #                 right_max = max(right_max, height[right])
# # # # # # #                 water += max(0, right_max - height[right])
# # # # # # #         return water

# # # # # # Решение Longest Increasing Subsequence
# # # # # # class LongestIncreasingSubsequence:
# # # # # #     def lengthOfLIS(self, nums):
# # # # # #         if not nums:
# # # # # #             return 0
# # # # # #         dp = [1] * len(nums)
# # # # # #         for i in range(1, len(nums)):
# # # # # #             for j in range(i):
# # # # # #                 if nums[i] > nums[j]:
# # # # # #                     dp[i] = max(dp[i], dp[j] + 1)
