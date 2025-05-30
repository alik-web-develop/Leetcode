# # # # Решение Two Sum
# # # # class TwoSum:
# # # #     def twoSum(self, nums, target):
# # # #         hash_map = {}
# # # #         for i, num in enumerate(nums):
# # # #             complement = target - num
# # # #             if complement in hash_map:
# # # #                 return [hash_map[complement], i]
# # # #             hash_map[num] = i
# # # #         return []

# # # # Решение Valid Parentheses
# # # # class ValidParentheses:
# # # #     def isValid(self, s):
# # # #         stack = []
# # # #         mapping = {')': '(', '}': '{', ']': '['}
# # # #         for char in s:
# # # #             if char in mapping:
# # # #                 top_element = stack.pop() if stack else '#'
# # # #                 if mapping[char] != top_element:
# # # #                     return False
# # # #             else:
# # # #                 stack.append(char)
# # # #         return not stack

# # # # Решение Reverse Linked List
# # # # class ListNode:
# # # #     def __init__(self, val=0, next=None):
# # # #         self.val = val
# # # #         self.next = next

# # # # class ReverseLinkedList:
# # # #     def reverseList(self, head):
# # # #         prev = None
# # # #         current = head
# # # #         while current:
# # # #             next_temp = current.next
# # # #             current.next = prev
# # # #             prev = current
# # # #             current = next_temp
# # # #         return prev

# # # # Решение Merge Two Sorted Lists
# # # # class MergeSortedLists:
# # # #     def mergeTwoLists(self, l1, l2):
# # # #         dummy = ListNode(0)
# # # #         current = dummy
# # # #         while l1 and l2:
# # # #             if l1.val < l2.val:
# # # #                 current.next = l1
# # # #                 l1 = l1.next
# # # #             else:
# # # #                 current.next = l2
# # # #                 l2 = l2.next
# # # #             current = current.next
# # # #         current.next = l1 if l1 else l2
# # # #         return dummy.next

# # # # Решение Binary Search
# # # # class BinarySearch:
# # # #     def search(self, nums, target):
# # # #         left, right = 0, len(nums) - 1
# # # #         while left <= right:
# # # #             mid = (left + right) // 2
# # # #             if nums[mid] == target:
# # # #                 return mid
# # # #             elif nums[mid] < target:
# # # #                 left = mid + 1
# # # #             else:
# # # #                 right = mid - 1
# # # #         return -1

# # # # Решение Climbing Stairs
# # # # class ClimbingStairs:
# # # #     def climbStairs(self, n):
# # # #         if n <= 2:
# # # #             return n
# # # #         dp = [0] * (n + 1)
# # # #         dp[1] = 1
# # # #         dp[2] = 2
# # # #         for i in range(3, n + 1):
# # # #             dp[i] = dp[i-1] + dp[i-2]
# # # #         return dp[n]

# # # # Решение Valid Palindrome
# # # # class ValidPalindrome:
# # # #     def isPalindrome(self, s):
# # # #         s = ''.join(c.lower() for c in s if c.isalnum())
# # # #         return s == s[::-1]

# # # # Решение Maximum Subarray
# # # # class MaximumSubarray:
# # # #     def maxSubArray(self, nums):
# # # #         max_sum = current_sum = nums[0]
# # # #         for num in nums[1:]:
# # # #             current_sum = max(num, current_sum + num)
# # # #             max_sum = max(max_sum, current_sum)
# # # #         return max_sum

# # # # Решение Single Number
# # # # class SingleNumber:
# # # #     def singleNumber(self, nums):
# # # #         result = 0
# # # #         for num in nums:
# # # #             result ^= num
# # # #         return result

# # # # Решение Move Zeroes
# # # # class MoveZeroes:
# # # #     def moveZeroes(self, nums):
# # # #         non_zero = 0
# # # #         for i in range(len(nums)):
# # # #             if nums[i] != 0:
# # # #                 nums[non_zero], nums[i] = nums[i], nums[non_zero]
# # # #                 non_zero += 1

# # # # Решение Longest Common Prefix
# # # # class LongestCommonPrefix:
# # # #     def longestCommonPrefix(self, strs):
# # # #         if not strs:
# # # #             return ""
# # # #         shortest = min(strs, key=len)
# # # #         for i, char in enumerate(shortest):
# # # #             for other in strs:
# # # #                 if other[i] != char:
# # # #                     return shortest[:i]
# # # #         return shortest

# # # # Решение Longest Palindromic Substring
# # # # class LongestPalindromicSubstring:
# # # #     def longestPalindrome(self, s):
# # # #         if not s:
# # # #             return ""
        
# # # #         start = 0
# # # #         max_length = 1
        
# # # #         def expand_around_center(left, right):
# # # #             nonlocal start, max_length
# # # #             while left >= 0 and right < len(s) and s[left] == s[right]:
# # # #                 if right - left + 1 > max_length:
# # # #                     start = left
# # # #                     max_length = right - left + 1
# # # #                 left -= 1
# # # #                 right += 1
        
# # # #         for i in range(len(s)):
# # # #             expand_around_center(i, i)  # для нечетной длины
# # # #             expand_around_center(i, i + 1)  # для четной длины
            
# # # #         return s[start:start + max_length]

# # # # Решение Merge K Sorted Lists
# # # # class MergeKSortedLists:
# # # #     def mergeKLists(self, lists):
# # # #         if not lists:
# # # #             return None
            
# # # #         import heapq
        
# # # #         # Создаем минимальную кучу
# # # #         heap = []
# # # #         for i, l in enumerate(lists):
# # # #             if l:
# # # #                 heapq.heappush(heap, (l.val, i, l))
                
# # # #         dummy = ListNode(0)
# # # #         current = dummy
        
# # # #         while heap:
# # # #             val, i, node = heapq.heappop(heap)
# # # #             current.next = node
# # # #             current = current.next
            
# # # #             if node.next:
# # # #                 heapq.heappush(heap, (node.next.val, i, node.next))
                
# # # #         return dummy.next

# # # # Решение Word Ladder
# # # # class WordLadder:
# # # #     def ladderLength(self, beginWord, endWord, wordList):
# # # #         if endWord not in wordList:
# # # #             return 0
            
# # # #         wordList = set(wordList)
# # # #         queue = [(beginWord, 1)]
# # # #         visited = {beginWord}
        
# # # #         while queue:
# # # #             word, length = queue.pop(0)
# # # #             if word == endWord:
# # # #                 return length
                
# # # #             for i in range(len(word)):
# # # #                 for c in 'abcdefghijklmnopqrstuvwxyz':
# # # #                     next_word = word[:i] + c + word[i+1:]
# # # #                     if next_word in wordList and next_word not in visited:
# # # #                         queue.append((next_word, length + 1))
# # # #                         visited.add(next_word)
                        
# # # #         return 0

# # # Решение Trapping Rain Water
# # # class TrappingRainWater:
# # #     def trap(self, height):
# # #         if not height:
# # #             return 0
# # #         left, right = 0, len(height) - 1
# # #         left_max, right_max = height[left], height[right]
# # #         water = 0
# # #         while left < right:
# # #             if left_max < right_max:
# # #                 left += 1
# # #                 left_max = max(left_max, height[left])
# # #                 water += max(0, left_max - height[left])
# # #             else:
# # #                 right -= 1
# # #                 right_max = max(right_max, height[right])
# # #                 water += max(0, right_max - height[right])
# # #         return water

# # Решение Longest Increasing Subsequence
# # class LongestIncreasingSubsequence:
# #     def lengthOfLIS(self, nums):
# #         if not nums:
# #             return 0
# #         dp = [1] * len(nums)
# #         for i in range(1, len(nums)):
# #             for j in range(i):
# #                 if nums[i] > nums[j]:
# #                     dp[i] = max(dp[i], dp[j] + 1)
# #         return max(dp)
# # объединение двух отсортированных массивов
# # class MergeSortedArrays:
# #     def merge(self, nums1, m, nums2, n):
# #         p1, p2, p = m - 1, n - 1, m + n - 1
# #         while p1 >= 0 and p2 >= 0:
# #             if nums1[p1] > nums2[p2]:
# #                 nums1[p] = nums1[p1]
# # Решение Course Schedule (Проверка возможности прохождения курсов)
# class CourseSchedule:
#     def canFinish(self, numCourses, prerequisites):
#         # Создаем граф
#         graph = [[] for _ in range(numCourses)]
#         visited = [0] * numCourses  # 0: не посещен, 1: в процессе, 2: посещен
        
#         # Строим граф
#         for course, prereq in prerequisites:
#             graph[course].append(prereq)
            
#         def hasCycle(course):
#             if visited[course] == 1:  # Обнаружен цикл
#                 return True
#             if visited[course] == 2:  # Уже посещен
#                 return False
                
#             visited[course] = 1  # Помечаем как "в процессе"
            
#             for prereq in graph[course]:
#                 if hasCycle(prereq):
#                     return True
                    
#             visited[course] = 2  # Помечаем как "посещен"
#             return False
            
#         # Проверяем каждый курс на наличие циклов
#         for course in range(numCourses):
#             if hasCycle(course):
#                 return False
#         return True

# # Решение Edit Distance (Расстояние Левенштейна)
# class EditDistance:
#     def minDistance(self, word1, word2):
#         m, n = len(word1), len(word2)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         # Инициализация первой строки и столбца
#         for i in range(m + 1):
#             dp[i][0] = i
#         for j in range(n + 1):
#             dp[0][j] = j
            
#         # Заполняем таблицу
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if word1[i-1] == word2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = min(dp[i-1][j],    # удаление
#                                  dp[i][j-1],    # вставка
#                                  dp[i-1][j-1]) + 1  # замена
#         return dp[m][n]

# # Решение Sliding Window Maximum
# class SlidingWindowMaximum:
#     def maxSlidingWindow(self, nums, k):
#         if not nums:
#             return []
            
#         from collections import deque
#         d = deque()
#         result = []
        
#         for i, num in enumerate(nums):
#             # Удаляем элементы, которые вышли за пределы окна
#             while d and d[0] <= i - k:
#                 d.popleft()
                
#             # Удаляем элементы, меньшие текущего
#             while d and nums[d[-1]] < num:
#                 d.pop()
                
#             d.append(i)
            
#             # Добавляем максимум в результат
#             if i >= k - 1:
#                 result.append(nums[d[0]])
                
#         return result

# # Решение Regular Expression Matching
# class RegularExpressionMatching:
#     def isMatch(self, s, p):
#         m, n = len(s), len(p)
#         dp = [[False] * (n + 1) for _ in range(m + 1)]
#         dp[0][0] = True
        
#         # Обработка паттернов вида a*
#         for j in range(1, n + 1):
#             if p[j-1] == '*':
#                 dp[0][j] = dp[0][j-2]
                
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if p[j-1] == '.' or p[j-1] == s[i-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 elif p[j-1] == '*':
#                     dp[i][j] = dp[i][j-2]  # пропускаем *
#                     if p[j-2] == '.' or p[j-2] == s[i-1]:
#                         dp[i][j] = dp[i][j] or dp[i-1][j]
                        
#         return dp[m][n]

