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
# # # # # #         return max(dp)
# # # # # # объединение двух отсортированных массивов
# # # # # # class MergeSortedArrays:
# # # # # #     def merge(self, nums1, m, nums2, n):
# # # # # #         p1, p2, p = m - 1, n - 1, m + n - 1
# # # # # #         while p1 >= 0 and p2 >= 0:
# # # # # #             if nums1[p1] > nums2[p2]:
# # # # # #                 nums1[p] = nums1[p1]
# # # # # # Решение Course Schedule (Проверка возможности прохождения курсов)
# # # # # class CourseSchedule:
# # # # #     def canFinish(self, numCourses, prerequisites):
# # # # #         # Создаем граф
# # # # #         graph = [[] for _ in range(numCourses)]
# # # # #         visited = [0] * numCourses  # 0: не посещен, 1: в процессе, 2: посещен
        
# # # # #         # Строим граф
# # # # #         for course, prereq in prerequisites:
# # # # #             graph[course].append(prereq)
            
# # # # #         def hasCycle(course):
# # # # #             if visited[course] == 1:  # Обнаружен цикл
# # # # #                 return True
# # # # #             if visited[course] == 2:  # Уже посещен
# # # # #                 return False
                
# # # # #             visited[course] = 1  # Помечаем как "в процессе"
            
# # # # #             for prereq in graph[course]:
# # # # #                 if hasCycle(prereq):
# # # # #                     return True
                    
# # # # #             visited[course] = 2  # Помечаем как "посещен"
# # # # #             return False
            
# # # # #         # Проверяем каждый курс на наличие циклов
# # # # #         for course in range(numCourses):
# # # # #             if hasCycle(course):
# # # # #                 return False
# # # # #         return True


# # # # # # Решение Sliding Window Maximum
# # # # # class SlidingWindowMaximum:
# # # # #     def maxSlidingWindow(self, nums, k):
# # # # #         if not nums:
# # # # #             return []
            
# # # # #         from collections import deque
# # # # #         d = deque()
# # # # #         result = []
        
# # # # #         for i, num in enumerate(nums):
# # # # #             # Удаляем элементы, которые вышли за пределы окна
# # # # #             while d and d[0] <= i - k:
# # # # #                 d.popleft()
                
# # # # #             # Удаляем элементы, меньшие текущего
# # # # #             while d and nums[d[-1]] < num:
# # # # #                 d.pop()
                
# # # # #             d.append(i)
            
# # # # #             # Добавляем максимум в результат
# # # # #             if i >= k - 1:
# # # # #                 result.append(nums[d[0]])

# # # # # Решение Container With Most Water
# # # # class ContainerWithMostWater:
# # # #     def maxArea(self, height):
# # # #         left, right = 0, len(height) - 1
# # # #         max_area = 0
        
# # # #         while left < right:
# # # #             # Вычисляем текущую площадь
# # # #             current_area = min(height[left], height[right]) * (right - left)
# # # #             max_area = max(max_area, current_area)
            
# # # #             # Перемещаем указатель с меньшей высотой
# # # #             if height[left] < height[right]:
# # # #                 left += 1
# # # #             else:
# # # #                 right -= 1
                
# # # #         return max_area

# # # # # Решение 3Sum
# # # # class ThreeSum:
# # # #     def threeSum(self, nums):
# # # #         nums.sort()
# # # #         result = []
        
# # # #         for i in range(len(nums) - 2):
# # # #             # Пропускаем дубликаты
# # # #             if i > 0 and nums[i] == nums[i-1]:
# # # #                 continue
                
# # # #             left, right = i + 1, len(nums) - 1
            
# # # #             while left < right:
# # # #                 current_sum = nums[i] + nums[left] + nums[right]
                
# # # #                 if current_sum == 0:
# # # #                     result.append([nums[i], nums[left], nums[right]])
# # # #                     # Пропускаем дубликаты
# # # #                     while left < right and nums[left] == nums[left + 1]:
# # # #                         left += 1
# # # #                     while left < right and nums[right] == nums[right - 1]:
# # # #                         right -= 1
# # # #                     left += 1
# # # #                     right -= 1
# # # #                 elif current_sum < 0:
# # # #                     left += 1
# # # #                 else:
# # # #                     right -= 1
                    
# # # #         return result

# # # # # Решение Remove Nth Node From End of List
# # # # class RemoveNthNodeFromEnd:
# # # #     def removeNthFromEnd(self, head, n):
# # # #         # Создаем фиктивный узел для обработки случая удаления первого элемента
# # # #         dummy = ListNode(0)
# # # #         dummy.next = head
        
# # # #         # Используем два указателя
# # # #         first = dummy
# # # #         second = dummy
        
# # # #         # Перемещаем first на n узлов вперед
# # # #         for _ in range(n + 1):
# # # #             first = first.next
            
# # # #         # Перемещаем оба указателя, пока first не достигнет конца
# # # #         while first:
            
        

# # # # Решение Find All Anagrams in String
# # # class FindAllAnagrams:
# # #     def findAnagrams(self, s, p):
# # #         if len(s) < len(p):
# # #             return []
            
# # #         p_count = [0] * 26
# # #         s_count = [0] * 26
# # #         result = []
        
# # #         # Заполняем начальные счетчики
# # #             p_count[ord(p[i]) - ord('a')] += 1
# # #             s_count[ord(s[i]) - ord('a')] += 1
            
            
# # #     def isValidSudoku(self, board):
# # #             for j in range(9):
# # #                 num = board[i][j]
# def target_num(nums,target):
#     result = []
#     for i in nums:
#         for y in nums[1:-1]:
#             print(i,y)
#             if i + y == target and i not in result and y not in result:
#                 return [nums.index(i),nums.index(y)]
#     return list(set(result))
# print(target_num(numbers,13))
from decimal import Decimal
# def two_string(str_num1,str_num2):
#     return str(Decimal(str_num1) + Decimal(str_num2))
num1 = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"
num2 = "1"
print(str(int(num1) + int(num2)))