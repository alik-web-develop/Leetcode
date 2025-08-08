# # # 151. Reverse Words in a String
# # # Given an input string s, reverse the order of the words.
# # # A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# # # Return a string of the words in reverse order concatenated by a single space.
# # # Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# # # x = "   Пример строки с пробелами   "
# # # def reverse_words(text):
# # #     result = []
# # #     [result.append(i) for i in text.split() if i]
# # #     result = result[::-1]
# # #     return (" ".join(result))
# # # print(reverse_words("  hello world  "))

# # # Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# # # x = [1,2,3,4,5,6,7,8,9,10]
# # # def reverse_linked(arr,left,right):
# # #     else:
# # #         arr[left-1:right-1] = arr[left-1:right-1][::-1]
# # #         return arr
# # # print(reverse_linked(x,3,8))

# # # вот тут литкод мой код не принял так как к нам оказывается приходит не просто list а ListNode это то ещё проблема так как там нету индексации типо вы не можете использовать element[left:right] из за этого пришлось голову морочить вот короче код который литкод принял
# # class Solution:
# #     def reverseBetween(self, head, left: int, right: int):
# #         dummy.next = head
# #         prev = dummy
        
# #         for _ in range(left - 1):
# #             prev = prev.next
        
# #         current = prev.next
        
# #         for _ in range(right - left):
# #             temp = current.next
# #             current.next = temp.next
# #             temp.next = prev.next
# #             prev.next = temp
        
# #         return dummy.next
# # print(Solution.reverseBetween())
# # #todo================================================================


# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# # # Решение Valid Anagram
# # class ValidAnagram:
# #     def isAnagram(self, s, t):
# #         if len(s) != len(t):
# #             return False
# #         return sorted(s) == sorted(t)

# # # Решение First Unique Character
# # class FirstUniqueCharacter:
# #     def firstUniqChar(self, s):
# #         count = {}
# #         for char in s:
# #             count[char] = count.get(char, 0) + 1
# #         for i, char in enumerate(s):
# #             if count[char] == 1:
# #                 return i
# #         return -1

# # # Решение Rotate Array
# # class RotateArray:
# #     def rotate(self, nums, k):
# #         k = k % len(nums)
# #         nums[:] = nums[-k:] + nums[:-k]

# # # Решение Contains Duplicate
# # class ContainsDuplicate:
# #     def containsDuplicate(self, nums):
# #         return len(nums) != len(set(nums))

# # # Примеры использования:
# # if __name__ == "__main__":
# #     # Two Sum
# #     two_sum = TwoSum()
# #     print(two_sum.twoSum([2, 7, 11, 15], 9))  # [0, 1]

# #     # Valid Parentheses
# #     valid_parens = ValidParentheses()
# #     print(valid_parens.isValid("()[]{}"))  # True

# #     # Binary Search
# #     binary_search = BinarySearch()
# #     print(binary_search.search([-1, 0, 3, 5, 9, 12], 9))  # 4

# #     # Climbing Stairs
# #     climbing = ClimbingStairs()
# #     print(climbing.climbStairs(3))  # 3

# #     # Valid Palindrome
# #     palindrome = ValidPalindrome()
# #     print(palindrome.isPalindrome("A man, a plan, a canal: Panama"))  # True

# #     # Longest Common Prefix
# #     prefix = LongestCommonPrefix()
# #     print(prefix.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"

# #     # Valid Anagram
# #     anagram = ValidAnagram()
# #     print(anagram.isAnagram("anagram", "nagaram"))  # True

# #     # First Unique Character
# #     unique = FirstUniqueCharacter()
# #     print(unique.firstUniqChar("leetcode"))  # 0

# # ===============================================
# # 1. Maximum Subarray (Kadane's Algorithm)
# # Given an integer array nums, find the subarray with the largest sum, and return its sum.
# class MaximumSubarray:
#     def maxSubArray(self, nums):
#         if not nums:
#             return 0
        
#         max_sum = current_sum = nums[0]
        
#         for num in nums[1:]:
#             current_sum = max(num, current_sum + num)
#             max_sum = max(max_sum, current_sum)
        
#         return max_sum

# # Пример использования:
# # max_sub = MaximumSubarray()
# # print(max_sub.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6

# # ===============================================
# # 2. Merge Two Sorted Lists
# # You are given the heads of two sorted linked lists list1 and list2.
# # Merge the two lists into one sorted list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MergeSortedLists:
#     def mergeTwoLists(self, list1, list2):
#         dummy = ListNode(0)
#         current = dummy
        
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
        
#         current.next = list1 if list1 else list2
#         return dummy.next

# # ===============================================
# # 3. Best Time to Buy and Sell Stock
# # You are given an array prices where prices[i] is the price of a given stock on the ith day.
# # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# class BestTimeToBuySell:
#     def maxProfit(self, prices):
#         if not prices:
#             return 0
        
#         min_price = prices[0]
#         max_profit = 0
        
#         for price in prices[1:]:
#             min_price = min(min_price, price)
#             max_profit = max(max_profit, price - min_price)
        
#         return max_profit

# # Пример использования:
# # profit = BestTimeToBuySell()
# # print(profit.maxProfit([7,1,5,3,6,4]))  # 5

# # ===============================================
# # 4. Valid Palindrome II
# # Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# class ValidPalindromeII:
#     def validPalindrome(self, s):
#         def is_palindrome(left, right):
#             while left < right:
#                 if s[left] != s[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True
        
#         left, right = 0, len(s) - 1
        
#         while left < right:
#             if s[left] != s[right]:
#                 return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
#             left += 1
#             right -= 1
        
#         return True

# # Пример использования:
# # palindrome_ii = ValidPalindromeII()
# # print(palindrome_ii.validPalindrome("abca"))  # True

# # ===============================================
# # 5. Move Zeroes
# # Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# class MoveZeroes:
#     def moveZeroes(self, nums):
#         non_zero_index = 0
        
#         # Перемещаем все ненулевые элементы в начало
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[non_zero_index] = nums[i]
#                 non_zero_index += 1
        
#         # Заполняем оставшиеся позиции нулями
#         for i in range(non_zero_index, len(nums)):
#             nums[i] = 0
        
#         return nums

# # Пример использования:
# # move_zeros = MoveZeroes()
# # nums = [0,1,0,3,12]
# # move_zeros.moveZeroes(nums)
# # print(nums)  # [1,3,12,0,0]





