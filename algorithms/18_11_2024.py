
# # 151. Reverse Words in a String
# # Given an input string s, reverse the order of the words.
# # A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# # Return a string of the words in reverse order concatenated by a single space.
# # Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# # x = "   Пример строки с пробелами   "
# # def reverse_words(text):
# #     result = []
# #     [result.append(i) for i in text.split() if i]
# #     result = result[::-1]
# #     return (" ".join(result))
# # print(reverse_words("  hello world  "))

# #todo================================================================
# # 92. Reverse Linked List II
# # Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# # x = [1,2,3,4,5,6,7,8,9,10]
# # def reverse_linked(arr,left,right):
# #     else:
# #         arr[left-1:right-1] = arr[left-1:right-1][::-1]
# #         return arr
# # print(reverse_linked(x,3,8))

# # вот тут литкод мой код не принял так как к нам оказывается приходит не просто list а ListNode это то ещё проблема так как там нету индексации типо вы не можете использовать element[left:right] из за этого пришлось голову морочить вот короче код который литкод принял
# class Solution:
#     def reverseBetween(self, head, left: int, right: int):
#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
        
#         for _ in range(left - 1):
#             prev = prev.next
        
#         current = prev.next
        
#         for _ in range(right - left):
#             temp = current.next
#             current.next = temp.next
#             temp.next = prev.next
#             prev.next = temp
        
#         return dummy.next
# print(Solution.reverseBetween())
# #todo================================================================


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # Решение Valid Anagram
# class ValidAnagram:
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)

# # Решение First Unique Character
# class FirstUniqueCharacter:
#     def firstUniqChar(self, s):
#         count = {}
#         for char in s:
#             count[char] = count.get(char, 0) + 1
#         for i, char in enumerate(s):
#             if count[char] == 1:
#                 return i
#         return -1

# # Решение Rotate Array
# class RotateArray:
#     def rotate(self, nums, k):
#         k = k % len(nums)
#         nums[:] = nums[-k:] + nums[:-k]

# # Решение Contains Duplicate
# class ContainsDuplicate:
#     def containsDuplicate(self, nums):
#         return len(nums) != len(set(nums))

# # Примеры использования:
# if __name__ == "__main__":
#     # Two Sum
#     two_sum = TwoSum()
#     print(two_sum.twoSum([2, 7, 11, 15], 9))  # [0, 1]

#     # Valid Parentheses
#     valid_parens = ValidParentheses()
#     print(valid_parens.isValid("()[]{}"))  # True

#     # Binary Search
#     binary_search = BinarySearch()
#     print(binary_search.search([-1, 0, 3, 5, 9, 12], 9))  # 4

#     # Climbing Stairs
#     climbing = ClimbingStairs()
#     print(climbing.climbStairs(3))  # 3

#     # Valid Palindrome
#     palindrome = ValidPalindrome()
#     print(palindrome.isPalindrome("A man, a plan, a canal: Panama"))  # True

#     # Longest Common Prefix
#     prefix = LongestCommonPrefix()
#     print(prefix.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"

#     # Valid Anagram
#     anagram = ValidAnagram()
#     print(anagram.isAnagram("anagram", "nagaram"))  # True

#     # First Unique Character
#     unique = FirstUniqueCharacter()
#     print(unique.firstUniqChar("leetcode"))  # 0

#     # Rotate Array
#     rotate = RotateArray()
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     rotate.rotate(nums, 3)
#     print(nums)  # [5, 6, 7, 1, 2, 3, 4]

#     # Contains Duplicate
#     duplicate = ContainsDuplicate()
#     print(duplicate.containsDuplicate([1, 2, 3, 1]))  # True
#     # Valid Anagram
#     anagram = ValidAnagram()
#     print(anagram.isAnagram("anagram", "nagaram"))  # True

#     # First Unique Character
#     unique = FirstUniqueCharacter()
#     print(unique.firstUniqChar("leetcode"))  # 0

#     # Rotate Array
#     rotate = RotateArray()
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     rotate.rotate(nums, 3)
#     print(nums)  # [5, 6, 7, 1, 2, 3, 4]

#     # Contains Duplicate
#     duplicate = ContainsDuplicate()
#     print(duplicate.containsDuplicate([1, 2, 3, 1]))  # True
#     # Valid Anagram
#     anagram = ValidAnagram()
#     print(anagram.isAnagram("anagram", "nagaram"))  # True

#     # First Unique Character
#     unique = FirstUniqueCharacter()
#     print(unique.firstUniqChar("leetcode"))  # 0

#     # Rotate Array
#     rotate = RotateArray()
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     rotate.rotate(nums, 3)
#     print(nums)  # [5, 6, 7, 1, 2, 3, 4]

#     # Contains Duplicate
#     duplicate = ContainsDuplicate()
#     print(duplicate.containsDuplicate([1, 2, 3, 1]))  # True
