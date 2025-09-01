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

# # # # # # # # Решение Binary Search
# # # # # # # #     def search(self, nums, target):
# # # # # # # #         left, right = 0, len(nums) - 1
# # # # # # # #         while left <= right:
# # # # # # # #             mid = (left + right) // 2
# # # # # # # #             if nums[mid] == target:
# # # # # # # #                 return mid
# # # # # # # #             elif nums[mid] < target:
# # # # # # # #                 left = mid + 1
# # # # # # # #             else:
# # # # # # # #                 right = mid - 1
# # # # # # # #         return -1

# # # # # # # # Решение Climbing Stairs
# # # # # # # # class ClimbingStairs:
# # # # # # # #     def climbStairs(self, n):
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
# # #         for i in range(len(p)):
# # #             p_count[ord(p[i]) - ord('a')] += 1
# # #             s_count[ord(s[i]) - ord('a')] += 1
            
# # #         if p_count == s_count:
# # #             result.append(0)
            
# # #         # Скользящее окно
# # #         for i in range(len(p), len(s)):
# # #             s_count[ord(s[i]) - ord('a')] += 1
# # #             s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
# # #             if p_count == s_count:
# # #                 result.append(i - len(p) + 1)
                
# # #         return result

# # # # Решение Valid Sudoku
# # # class ValidSudoku:
# # #     def isValidSudoku(self, board):
# # #         rows = [set() for _ in range(9)]
# # #         cols = [set() for _ in range(9)]
# # #         boxes = [set() for _ in range(9)]
        
# # #         for i in range(9):
# # #             for j in range(9):
# # #                 num = board[i][j]
# # #                 if num == '.':
# # #                     continue
                    
# # #                 box_idx = (i // 3) * 3 + j // 3
                
# # #                 if (num in rows[i] or 
# # #                     num in cols[j] or 
# # #                     num in boxes[box_idx]):
# # #                     return False
                    
# # #                 rows[i].add(num)
# # #                 cols[j].add(num)
# # #                 boxes[box_idx].add(num)
                
# # #         return True

# # # # Решение Maze Path Finder
# # # class MazePathFinder:
# # #     def findPath(self, maze, start, end):
# # #         if not maze or not maze[0]:
# # #             return []
            
# # #         rows, cols = len(maze), len(maze[0])
# # #         visited = set()
# # #         path = []
        
# # #         def dfs(x, y):
# # #             if (x, y) == end:
# # #                 return True
                
# # #             if (0 <= x < rows and 0 <= y < cols and 
# # #                 maze[x][y] == 0 and (x, y) not in visited):
# # #                 visited.add((x, y))
# # #                 path.append((x, y))
                
# # #                 for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
# # #                     if dfs(x + dx, y + dy):
# # #                         return True
                        
# # #                 path.pop()
# # #                 return False
                
# # #         if dfs(start[0], start[1]):
# # #             return path
# # #         return []

# # # # Решение String Compression
# # # class StringCompression:
# # #     def compress(self, chars):
# # #         if not chars:
# # #             return 0
            
# # #         write = 0
# # #         read = 0
        
# # #         while read < len(chars):
# # #             current_char = chars[read]
# # #             count = 0
            
# # #             while read < len(chars) and chars[read] == current_char:
# # #                 read += 1
# # #                 count += 1
                
# # #             chars[write] = current_char
# # #             write += 1
            
# # #             if count > 1:
# # #                 for digit in str(count):
# # #                     chars[write] = digit
# # #                     write += 1
                    
# # #         return write

# # # # Решение Lowest Common Ancestor in Binary Tree
# # # class TreeNode:
# # #     def __init__(self, x):
# # #         self.val = x
# # #         self.left = None
# # #         self.right = None

# # # class LowestCommonAncestor:
# # #     def lowestCommonAncestor(self, root, p, q):
# # #         if not root or root == p or root == q:
# # #             return root
            
# # #         left = self.lowestCommonAncestor(root.left, p, q)
# # #         right = self.lowestCommonAncestor(root.right, p, q)
        
# # #         if left and right:
# # #             return root
# # #         return left if left else right

# # # Решение Combination Sum
# # class CombinationSum:
# #     def combinationSum(self, candidates, target):
# #         result = []
        
# #         def backtrack(remain, combo, start):
# #             if remain == 0:
# #                 result.append(list(combo))
# #                 return
# #             elif remain < 0:
# #                 return
                
# #             for i in range(start, len(candidates)):
# #                 combo.append(candidates[i])
# #                 backtrack(remain - candidates[i], combo, i)
# #                 combo.pop()
                
# #         backtrack(target, [], 0)
# #         return result

# # # Решение Validate Binary Search Tree
# # class ValidateBST:
# #     def isValidBST(self, root):
# #         def validate(node, low=float('-inf'), high=float('inf')):
# #             if not node:
# #                 return True
                
# #             if node.val <= low or node.val >= high:
# #                 return False
                
# #             return (validate(node.left, low, node.val) and 
# #                     validate(node.right, node.val, high))
                    
# #         return validate(root)

# # # Решение Median of Two Sorted Arrays
# # class MedianOfSortedArrays:
# #     def findMedianSortedArrays(self, nums1, nums2):
# #         if len(nums1) > len(nums2):
# #             nums1, nums2 = nums2, nums1
            
# #         x, y = len(nums1), len(nums2)
# #         low, high = 0, x
        
# #         while low <= high:
# #             partitionX = (low + high) // 2
# #             partitionY = (x + y + 1) // 2 - partitionX
            
# #             maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
# #             minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
# #             maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
# #             minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
# #             if maxLeftX <= minRightY and maxLeftY <= minRightX:
# #                 if (x + y) % 2 == 0:
# #                     return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
# #                 else:
# #                     return max(maxLeftX, maxLeftY)
# #             elif maxLeftX > minRightY:
# #                 high = partitionX - 1
# #             else:
# #                 low = partitionX + 1

# # # Решение Permutations
# # class Permutations:
# #     def permute(self, nums):
# #         result = []
        
# #         def backtrack(start):
# #             if start == len(nums):
# #                 result.append(nums[:])
# #                 return
                
# #             for i in range(start, len(nums)):
# #                 nums[start], nums[i] = nums[i], nums[start]
# #                 backtrack(start + 1)
# #                 nums[start], nums[i] = nums[i], nums[start]
                
# #         backtrack(0)
# #         return result

# # # Решение Max Area of Island
# # class MaxAreaOfIsland:
# #     def maxAreaOfIsland(self, grid):
# #         if not grid:
# #             return 0
            
# #         max_area = 0
# #         rows, cols = len(grid), len(grid[0])
        
# #         def dfs(r, c):
# #             if (r < 0 or r >= rows or 
# #                 c < 0 or c >= cols or 
# #                 grid[r][c] == 0):
# #                 return 0
                
# #             grid[r][c] = 0  # Помечаем как посещенный
# #             area = 1
            
# #             # Проверяем все 4 направления
# #             area += dfs(r + 1, c)
# #             area += dfs(r - 1, c)
# #             area += dfs(r, c + 1)
# #             area += dfs(r, c - 1)
            
# #             return area
            
# #         for r in range(rows):
# #             for c in range(cols):
# #                 if grid[r][c] == 1:
# #                     max_area = max(max_area, dfs(r, c))
                    
# #         return max_area

# # Решение QuickSort
# class QuickSort:
#     def quickSort(self, arr):
#         if len(arr) <= 1:
#             return arr
            
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
        
#         return self.quickSort(left) + middle + self.quickSort(right)

# # Решение Binary Search Tree
# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
        
#     def insert(self, val):
#         if not self.root:
#             self.root = TreeNode(val)
#             return
            
#         def _insert(node, val):
#             if val < node.val:
#                 if node.left:
#                     _insert(node.left, val)
#                 else:
#                     node.left = TreeNode(val)
#             else:
#                 if node.right:
#                     _insert(node.right, val)
#                 else:
#                     node.right = TreeNode(val)
                    
#         _insert(self.root, val)
        
#     def search(self, val):
#         def _search(node, val):
#             if not node:
#                 return False
#             if node.val == val:
#                 return True
#             if val < node.val:
#                 return _search(node.left, val)
#             return _search(node.right, val)
            
#         return _search(self.root, val)

# # Решение Dijkstra's Algorithm
# class Dijkstra:
#     def dijkstra(self, graph, start):
#         distances = {node: float('infinity') for node in graph}
#         distances[start] = 0
#         unvisited = set(graph.keys())
        
#         while unvisited:
#             current = min(unvisited, key=lambda node: distances[node])
#             if distances[current] == float('infinity'):
#                 break
                
#             unvisited.remove(current)
            
#             for neighbor, weight in graph[current].items():
#                 distance = distances[current] + weight
#                 if distance < distances[neighbor]:
#                     distances[neighbor] = distance
                    
#         return distances

# # Решение Knapsack Problem
# class Knapsack:
#     def knapsack(self, weights, values, capacity):
#         n = len(weights)
#         dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        
#         for i in range(1, n + 1):
#             for w in range(capacity + 1):
#                 if weights[i-1] <= w:
#                     dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
#                 else:
#                     dp[i][w] = dp[i-1][w]
                    
#         return dp[n][capacity]

# # Решение Topological Sort
# class TopologicalSort:
#     def topologicalSort(self, graph):
#         visited = set()
#         temp = set()
#         order = []
        
#         def visit(node):
#             if node in temp:
#                 raise ValueError("Graph contains a cycle")
#             if node in visited:
#                 return
                
#             temp.add(node)
            
#             for neighbor in graph.get(node, []):
#                 visit(neighbor)
                
#             temp.remove(node)
#             visited.add(node)
#             order.append(node)
            
#         for node in graph:
#             if node not in visited:
#                 visit(node)
                
#         return order[::-1]



    





