# # # # # # # # l = ["Hello", "abc","test","a","ab","world"]

# # # # # # # # def bubble_sort(u_ns):
# # # # # # # #     sorted = False
# # # # # # # #     while not sorted:
# # # # # # # #         sorted = True
# # # # # # # #         for i in range(len(u_ns)-1):
# # # # # # # #             if len(u_ns[i]) > len(u_ns[i+1]):
# # # # # # # #                 u_ns[i], u_ns[i + 1] = u_ns[i+1], u_ns[i]
# # # # # # # #                 sorted = False

# # # # # # # # bubble_sort(l)
# # # # # # # # print(l)
# # # # # # # # def pyr(num,num2=1):
# # # # # # # #     print(" "*num2 + "*"*(num-num2))
# # # # # # # #     if num > num2:
# # # # # # # #         return pyr(num-1,num2+1)
# # # # # # # #     else:
# # # # # # # #         return ""
# # # # # # # # pyr(10)

# # # # # # # def factorial(n):
# # # # # # #     if n == 0 or n == 1:
# # # # # # #         return 1
# # # # # # #     return n * factorial(n-1)

# # # # # # # # Пример использования:
# # # # # # # # print(factorial(5))  # Выведет: 120

# # # # # # # def is_prime(n):
# # # # # # #     if n < 2:
# # # # # # #         return False
# # # # # # #     for i in range(2, int(n ** 0.5) + 1):
# # # # # # #         if n % i == 0:
# # # # # # #             return False
# # # # # # #     return True

# # # # # # # # Пример использования:
# # # # # # # # print(is_prime(17))  # Выведет: True
# # # # # # # # print(is_prime(20))  # Выведет: False

# # # # # # # def fibonacci(n):
# # # # # # #     if n <= 0:
# # # # # # #         return []
# # # # # # #     elif n == 1:
# # # # # # #         return [0]
# # # # # # #     fib = [0, 1]
# # # # # # #     for i in range(2, n):
# # # # # # #         fib.append(fib[i-1] + fib[i-2])
# # # # # # #     return fib

# # # # # # # # Пример использования:
# # # # # # # # print(fibonacci(10))  # Выведет: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# # # # # # # def is_palindrome(s):
# # # # # # #     # Удаляем пробелы и приводим к нижнему регистру
# # # # # # #     s = ''.join(c.lower() for c in s if c.isalnum())
# # # # # # #     return s == s[::-1]

# # # # # # # # Пример использования:
# # # # # # # # print(is_palindrome("A man, a plan, a canal: Panama"))  # Выведет: True
# # # # # # # # print(is_palindrome("hello"))  # Выведет: False

# # # # # # # def gcd(a, b):
# # # # # # #     while b:
# # # # # # #         a, b = b, a % b
# # # # # # #     return a

# # # # # # # # Пример использования:
# # # # # # # # print(gcd(48, 18))  # Выведет: 6
# # # # # # # # print(gcd(54, 24))  # Выведет: 6

# # # # # # # def two_sum(nums, target):
# # # # # # #     lookup = {}
# # # # # # #     for i, num in enumerate(nums):
# # # # # # #         if target - num in lookup:
# # # # # # #             return [lookup[target - num], i]
# # # # # # #         lookup[num] = i
# # # # # # #     return []

# # # # # # # # Пример использования:
# # # # # # # # print(two_sum([2, 7, 11, 15], 9))  # Выведет: [0, 1]

# # # # # # # class Bank:
# # # # # # #     def __init__(self, bank_name: str, account_id: int, pin: int):
# # # # # # #         self._bank_name = bank_name
# # # # # # #         self._bank_id = account_id
# # # # # # #         self._pin = pin
# # # # # # #         self._balance = 0

# # # # # # #     def __str__(self):
# # # # # # #         return f"You have a account on this bank- '{self._bank_name}'"

# # # # # # #     def print_msg(self, msg):
# # # # # # #         print("\n")
# # # # # # #         print("*" * 20)
# # # # # # #         print(msg)
# # # # # # #         print("*" * 20)
# # # # # # #         print("\n")

# # # # # # #     def validate_account_exist(self, account_id, pin) -> bool:
# # # # # # #         if self._bank_id == account_id and self._pin == pin:
# # # # # # #             return True
# # # # # # #         self.print_msg(f"No account exist on id {account_id}")
# # # # # # #         return False

# # # # # # #     def invest(self, amount: float, account_id: int, pin: int) -> bool:
# # # # # # #         """Вклад в личный счет"""
# # # # # # #         if self.validate_account_exist(account_id, pin):
# # # # # # #             self._balance = self._balance + amount
# # # # # # #             self.print_msg(
# # # # # # #                 f" SUCCESFULT INVEST your new balance {self._balance}")
# # # # # # #             return True
# # # # # # #         return False

# # # # # # #     def withdraw(self, amount: float, account_id: int, pin: int) -> bool:
# # # # # # #         if self.validate_account_exist(account_id, pin):
# # # # # # #             self._balance = self._balance - amount
# # # # # # #             self.print_msg(
# # # # # # #                 f" SUCCESLUFY WITHDRAW your new balance {self._balance}")
# # # # # # #             return True


# # # # # # # class HamkorBank(Bank):
# # # # # # #     def __init__(self, bank_name: str, account_id: int, pin: int, location: str):
# # # # # # #         super().__init__(bank_name, account_id, pin)
# # # # # # #         self.location = location


# # # # # # # account_id = 123908  # int!
# # # # # # # pin = 123123         # int!
# # # # # # # bank_balance = HamkorBank("Hamkor bank", account_id, pin, "Amir temur 30 st: Registan")
# # # # # # # print(bank_balance)

# # # # # # # bank_balance.invest(30000.00, account_id, pin)

# # # # # # # Binary Search
# # # # # # # def binary_search(arr, target):
# # # # # # #     left, right = 0, len(arr) - 1
# # # # # # #     while left <= right:
# # # # # # #         mid = (left + right) // 2
# # # # # # #         if arr[mid] == target:
# # # # # # #             return mid
# # # # # # #         elif arr[mid] < target:
# # # # # # #             left = mid + 1
# # # # # # #         else:
# # # # # # #             right = mid - 1
# # # # # # #     return -1

# # # # # # # # Quick Sort
# # # # # # # def quick_sort(arr):
# # # # # # #     if len(arr) <= 1:
# # # # # # #         return arr
# # # # # # #     pivot = arr[len(arr) // 2]
# # # # # # #     left = [x for x in arr if x < pivot]
# # # # # # #     middle = [x for x in arr if x == pivot]
# # # # # # #     right = [x for x in arr if x > pivot]
# # # # # # #     return quick_sort(left) + middle + quick_sort(right)

# # # # # # # # Merge Sort
# # # # # # # def merge_sort(arr):
# # # # # # #     if len(arr) <= 1:
# # # # # # #         return arr
# # # # # # #     mid = len(arr) // 2
# # # # # # #     left_half = arr[:mid]
# # # # # # #     right_half = arr[mid:]

# # # # # # #     left_half = merge_sort(left_half)
# # # # # # #     right_half = merge_sort(right_half)

# # # # # # #     return merge(left_half, right_half)

# # # # # # # def merge(left, right):
# # # # # # #     merged = []
# # # # # # #     i, j = 0, 0
# # # # # # #     while i < len(left) and j < len(right):
# # # # # # #         if left[i] < right[j]:
# # # # # # #             merged.append(left[i])
# # # # # # #             i += 1
# # # # # # #         else:
# # # # # # #             merged.append(right[j])
# # # # # # #             j += 1
# # # # # # #     while i < len(left):
# # # # # # #         merged.append(left[i])
# # # # # # #         i += 1
# # # # # # #     while j < len(right):
# # # # # # #         merged.append(right[j])
# # # # # # #         j += 1
# # # # # # #     return merged

# # # # # # # # BFS (Breadth-First Search) for a graph (represented as an adjacency list)
# # # # # # # from collections import deque

# # # # # # # def bfs(graph, start_node):
# # # # # # #     visited = set()
# # # # # # #     queue = deque([start_node])
# # # # # # #     visited.add(start_node)

# # # # # # #     result = []
# # # # # # #     while queue:
# # # # # # #         node = queue.popleft()
# # # # # # #         result.append(node)
# # # # # # #         for neighbor in graph.get(node, []):
# # # # # # #             if neighbor not in visited:
# # # # # # #                 visited.add(neighbor)
# # # # # # #                 queue.append(neighbor)
# # # # # # #     return result

# # # # # # # # DFS (Depth-First Search) for a graph (represented as an adjacency list)
# # # # # # # def dfs(graph, start_node, visited=None, result=None):
# # # # # # #     if visited is None:
# # # # # # #         visited = set()
# # # # # # #     if result is None:
# # # # # # #         result = []

# # # # # # #     visited.add(start_node)
# # # # # # #     result.append(start_node)

# # # # # # # Dijkstra's Algorithm (для нахождения кратчайшего пути в графе)
# # # # # # import heapq

# # # # # # def dijkstra(graph, start):
# # # # # #     distances = {node: float('inf') for node in graph}
# # # # # #     distances[start] = 0
# # # # # #     priority_queue = [(0, start)] # (distance, node)

# # # # # #     while priority_queue:
# # # # # #         current_distance, current_node = heapq.heappop(priority_queue)

# # # # # #         # Если мы уже нашли более короткий путь
# # # # # #         if current_distance > distances[current_node]:
# # # # # #             continue

# # # # # #         for neighbor, weight in graph[current_node].items():
# # # # # #             distance = current_distance + weight

# # # # # #             # Если найден более короткий путь
# # # # # #             if distance < distances[neighbor]:
# # # # # #                 distances[neighbor] = distance
# # # # # #                 heapq.heappush(priority_queue, (distance, neighbor))
# # # # # #     return distances

# # # # # # # Пример использования:
# # # # # # # graph = {
# # # # # # #     'A': {'B': 1, 'C': 4},
# # # # # # #     'B': {'A': 1, 'C': 2, 'D': 5},
# # # # # # #     'C': {'A': 4, 'B': 2, 'D': 1},
# # # # # # #     'D': {'B': 5, 'C': 1}
# # # # # # # }
# # # # # # # print(dijkstra(graph, 'A')) # Выведет: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

# # # # # # # Kadane's Algorithm (для нахождения максимальной суммы подмассива)
# # # # # # def kadane(arr):
# # # # # #     max_so_far = arr[0]
# # # # # #     current_max = arr[0]

# # # # # #     for i in range(1, len(arr)):
# # # # # #         current_max = max(arr[i], current_max + arr[i])
# # # # # #         max_so_far = max(max_so_far, current_max)

# # # # # #     return max_so_far

# # # # # # # Пример использования:
# # # # # # # print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Выведет: 6 (подмассив [4, -1, 2, 1])

# # # # # # # Topological Sort (для ориентированных ациклических графов)
# # # # # # from collections import defaultdict, deque

# # # # # # def topological_sort(graph):
# # # # # #     in_degree = defaultdict(int)
# # # # # #     for u in graph:
# # # # # #         for v in graph[u]:
# # # # # #             in_degree[v] += 1
# # # # # #     
# # # # # #     queue = deque([u for u in graph if in_degree[u] == 0])
# # # # # #     result = []

# # # # # #     while queue:
# # # # # #         u = queue.popleft()
# # # # # #         result.append(u)
# # # # # #         for v in graph[u]:
# # # # # #             in_degree[v] -= 1
# # # # # #             if in_degree[v] == 0:
# # # # # #                 queue.append(v)
# # # # # #     
# # # # # #     # Проверяем на цикл (если не все вершины были включены)
# # # # # #     if len(result) == len(graph):
# # # # # #         return result
# # # # # #     else:
# # # # # #         return [] # Граф содержит цикл

# # # # # # # Пример использования:
# # # # # # # graph = {
# # # # # # #     'A': ['C'],
# # # # # # #     'B': ['C', 'D'],
# # # # # # #     'C': ['E'],
# # # # # # #     'D': ['E'],
# # # # # # #     'E': []
# # # # # # # }
# # # # # # # print(topological_sort(graph)) # Выведет: ['A', 'B', 'C', 'D', 'E'] или ['B', 'A', 'C', 'D', 'E']

# # # # # # # Longest Common Subsequence (LCS) (для нахождения самой длинной общей подпоследовательности)
# # # # # # def lcs(X, Y):
# # # # # #     m = len(X)
# # # # # #     n = len(Y)

# # # # # #     L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

# # # # # #     for i in range(m + 1):
# # # # # #         for j in range(n + 1):
# # # # # #             if i == 0 or j == 0:
# # # # # #                 L[i][j] = 0
# # # # # #             elif X[i-1] == Y[j-1]:
# # # # # #                 L[i][j] = L[i-1][j-1] + 1
# # # # # #             else:
# # # # # #                 L[i][j] = max(L[i-1][j], L[i][j-1])
# # # # # #     return L[m][n]

# # # # # # # Пример использования:
# # # # # # # X = "AGGTAB"
# # # # # # # Y = "GXTXAYB"
# # # # # # # print(lcs(X, Y)) # Выведет: 4 (GTAB)

# # # # # # # Floyd-Warshall Algorithm (для нахождения кратчайших путей между всеми парами вершин в взвешенном ориентированном графе)
# # # # # # def floyd_warshall(graph):
# # # # # #     num_vertices = len(graph)
# # # # # #     dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

# # # # # #     for k in range(num_vertices):
# # # # # #         for i in range(num_vertices):
# # # # # #             for j in range(num_vertices):
# # # # # #                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
# # # # # #     return dist

# # # # # # # Пример использования:
# # # # # # # INF = float('inf')
# # # # # # # graph = [
# # # # # # #     [0, 3, INF, 5],
# # # # # # #     [2, 0, INF, 4],
# # # # # # #     [INF, 1, 0, INF],
# # # # # # #     [INF, INF, 2, 0]
# # # # # # # ]
# # # # # # # print(floyd_warshall(graph)) # Выведет:
# # # # # # # # [[0, 3, 7, 5],
# # # # # # # #  [2, 0, 6, 4],
# # # # # # # #  [3, 1, 0, 5],
# # # # # # # #  [5, 3, 2, 0]]

# # # # # # # Kruskal's Algorithm (для нахождения минимального остовного дерева)

# # # # # class DisjointSet:
# # # # #     def __init__(self, vertices):
# # # # #         self.parent = {v: v for v in vertices}
# # # # #         self.rank = {v: 0 for v in vertices}

# # # # #     def find(self, item):
# # # # #         if self.parent[item] == item:
# # # # #             return item
# # # # #         self.parent[item] = self.find(self.parent[item])
# # # # #         return self.parent[item]

# # # # #     def union(self, set1, set2):
# # # # #         root1 = self.find(set1)
# # # # #         root2 = self.find(set2)
# # # # #         if root1 != root2:
# # # # #             if self.rank[root1] < self.rank[root2]:
# # # # #                 self.parent[root1] = root2
# # # # #             elif self.rank[root1] > self.rank[root2]:
# # # # #                 self.parent[root2] = root1
# # # # #             else:
# # # # #                 self.parent[root2] = root1
# # # # #                 self.rank[root1] += 1
# # # # #             return True
# # # # #         return False

# # # # # def kruskal(graph):
# # # # #     minimum_spanning_tree = []
# # # # #     edges = []
# # # # #     for u in graph:
# # # # #         for v, weight in graph[u].items():
# # # # #             edges.append((weight, u, v))
# # # # #     edges.sort()

# # # # #     vertices = list(graph.keys())
# # # # #     ds = DisjointSet(vertices)

# # # # #     for weight, u, v in edges:
# # # # #         if ds.union(u, v):
# # # # #             minimum_spanning_tree.append((u, v, weight))
# # # # #     return minimum_spanning_tree

# # # # # # Пример использования:
# # # # # # graph = {
# # # # # #     'A': {'B': 1, 'C': 4},
# # # # # #     'B': {'A': 1, 'C': 2, 'D': 5},
# # # # # #     'C': {'A': 4, 'B': 2, 'D': 1},
# # # # # #     'D': {'B': 5, 'C': 1}
# # # # # # }
# # # # # # print(kruskal(graph)) # Выведет: [('A', 'B', 1), ('C', 'D', 1), ('B', 'C', 2)]


# # # # # # Prim's Algorithm (для нахождения минимального остовного дерева)
# # # # # import heapq

# # # # # def prim(graph, start_node):
# # # # #     min_spanning_tree = []
# # # # #     visited = set()
# # # # #     # (weight, from_node, to_node)
# # # # #     priority_queue = [(0, start_node, None)]

# # # # #     while priority_queue:
# # # # #         weight, current_node, from_node = heapq.heappop(priority_queue)

# # # # #         if current_node in visited:
# # # # #             continue

# # # # #         visited.add(current_node)
# # # # #         if from_node is not None:
# # # # #             min_spanning_tree.append((from_node, current_node, weight))

# # # # #         for neighbor, edge_weight in graph[current_node].items():
# # # # #             if neighbor not in visited:
# # # # #                 heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

# # # # #     return min_spanning_tree

# # # # # # Пример использования:
# # # # # # graph = {
# # # # # #     'A': {'B': 1, 'C': 4},
# # # # # #     'B': {'A': 1, 'C': 2, 'D': 5},
# # # # # #     'C': {'A': 4, 'B': 2, 'D': 1},
# # # # # #     'D': {'B': 5, 'C': 1}
# # # # # # }
# # # # # # print(prim(graph, 'A')) # Выведет: [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]


# # # # # # Bellman-Ford Algorithm (для поиска кратчайшего пути с отрицательными весами)
# # # # # def bellman_ford(edges, num_vertices, start_node):
# # # # #     distances = {i: float('inf') for i in range(num_vertices)}
# # # # #     distances[start_node] = 0

# # # # #     for _ in range(num_vertices - 1):
# # # # #         for u, v, weight in edges:
# # # # #             if distances[u] != float('inf') and distances[u] + weight < distances[v]:
# # # # #                 distances[v] = distances[u] + weight

# # # # #     # Проверка на отрицательные циклы
# # # # #     for u, v, weight in edges:
# # # # #         if distances[u] != float('inf') and distances[u] + weight < distances[v]:
# # # # #             return {} # Обнаружен отрицательный цикл

# # # # #     return distances

# # # # # # Пример использования:
# # # # # # edges = [
# # # # # #     (0, 1, -1), (0, 2, 4),
# # # # # #     (1, 2, 3), (1, 3, 2), (1, 4, 2),
# # # # # #     (3, 2, 5), (3, 1, 1),
# # # # # #     (4, 3, -3)
# # # # # # ]
# # # # # # num_vertices = 5
# # # # # # start_node = 0
# # # # # # print(bellman_ford(edges, num_vertices, start_node)) # Выведет: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}


# # # # # # Longest Increasing Subsequence (LIS) (для нахождения самой длинной возрастающей подпоследовательности)
# # # # # def longest_increasing_subsequence(arr):
# # # # #     if not arr:
# # # # #         return 0

# # # # #     tails = []
# # # # #     for num in arr:
# # # # #         i = 0
# # # # #         j = len(tails)
# # # # #         while i < j:
# # # # #             m = (i + j) // 2
# # # # #             if tails[m] < num:
# # # # #                 i = m + 1
# # # # #             else:
# # # # #                 j = m
# # # # #         if i == len(tails):
# # # # #             tails.append(num)
# # # # #         else:
# # # # #             tails[i] = num
# # # # #     return len(tails)

# # # # # # Пример использования:
# # # # # # print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])) # Выведет: 4 (например, [2, 3, 7, 18] или [2, 5, 7, 18])


# # # # # # Knapsack Problem (0/1 Knapsack) (решение задачи о рюкзаке)
# # # # # def knapsack(values, weights, capacity):
# # # # #     n = len(values)
# # # # #     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# # # # #     for i in range(1, n + 1):
# # # # #         for w in range(1, capacity + 1):
# # # # #             if weights[i-1] <= w:
# # # # #                 dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
# # # # #             else:
# # # # #                 dp[i][w] = dp[i-1][w]
# # # # #     return dp[n][capacity]

# # # # # # Пример использования:
# # # # # # values = [60, 100, 120]
# # # # # # weights = [10, 20, 30]
# # # # # # capacity = 50
# # # # # # print(knapsack(values, weights, capacity)) # Выведет: 220 (взяты предметы со стоимостью 100 и 120)


# # # # # Aho-Corasick Algorithm (для поиска множества шаблонов в тексте)
# # # # from collections import deque

# # # # class AhoCorasick:
# # # #     def __init__(self, patterns):
# # # #         self.trie = {'__children__': {}, '__output__': [], '__fail__': None}
# # # #         self._build_trie(patterns)
# # # #         self._build_failure_links()

# # # #     def _build_trie(self, patterns):
# # # #         for pattern in patterns:
# # # #             node = self.trie
# # # #             for char in pattern:
# # # #                 if char not in node['__children__']:
# # # #                     node['__children__'][char] = {'__children__': {}, '__output__': [], '__fail__': None}
# # # #                 node = node['__children__'][char]
# # # #             node['__output__'].append(pattern)

# # # #     def _build_failure_links(self):
# # # #         queue = deque()
# # # #         # Корень имеет failure link на себя, но для удобства установим на None
# # # #         # Его потомки имеют failure link на корень
# # # #         for char, child in self.trie['__children__'].items():
# # # #             child['__fail__'] = self.trie
# # # #             queue.append(child)

# # # #         while queue:
# # # #             current_node = queue.popleft()
# # # #             for char, next_node in current_node['__children__'].items():
# # # #                 failure_node = current_node['__fail__']
# # # #                 while failure_node and char not in failure_node['__children__']:
# # # #                     failure_node = failure_node['__fail__']
                
# # # #                 if failure_node and char in failure_node['__children__']:
# # # #                     next_node['__fail__'] = failure_node['__children__'][char]
# # # #                 else:
# # # #                     next_node['__fail__'] = self.trie # Если нет совпадения, то на корень

# # # #                 # Добавляем output из failure link
# # # #                 next_node['__output__'].extend(next_node['__fail__']['__output__'])
# # # #                 queue.append(next_node)

# # # #     def search(self, text):
# # # #         results = []
# # # #         node = self.trie
# # # #         for i, char in enumerate(text):
# # # #             while node and char not in node['__children__']:
# # # #                 node = node['__fail__']
            
# # # #             if node and char in node['__children__']:
# # # #                 node = node['__children__'][char]
# # # #             else:
# # # #                 node = self.trie # Если нет совпадения, то на корень

# # # #             for pattern in node['__output__']:
# # # #                 results.append((i - len(pattern) + 1, pattern))
# # # #         return results

# # # # # Пример использования:
# # # # # patterns = ["he", "she", "his", "hers"]
# # # # # text = "ahishers"
# # # # # ac_automaton = AhoCorasick(patterns)
# # # # # print(ac_automaton.search(text)) # Выведет: [(1, 'his'), (3, 'he'), (4, 'she'), (4, 'hers')]


# # # # # Z-Algorithm (для поиска всех вхождений шаблона в текст)
# # # # def z_algorithm(s):
# # # #     n = len(s)
# # # #     z = [0] * n
# # # #     l, r = 0, 0
# # # #     for i in range(1, n):
# # # #         if i <= r:
# # # #             z[i] = min(r - i + 1, z[i - l])
# # # #         while i + z[i] < n and s[z[i]] == s[i + z[i]]:
# # # #             z[i] += 1
# # # #         if i + z[i] - 1 > r:
# # # #             l, r = i, i + z[i] - 1
# # # #     return z

# # # # # Пример использования:
# # # # # text = "aabxaabxcaabxaabx"
# # # # # pattern = "aabx"
# # # # # combined = pattern + "$" + text # Используем уникальный разделитель
# # # # # z_values = z_algorithm(combined)
# # # # # occurrences = []
# # # # # for i in range(len(pattern) + 1, len(combined)):
# # # # #     if z_values[i] == len(pattern):
# # # # #         occurrences.append(i - (len(pattern) + 1))
# # # # # print(occurrences) # Выведет: [0, 4, 11]


# # # # # Manacher's Algorithm (для нахождения самой длинной палиндромной подстроки)
# # # # def manacher(text):
# # # #     # Преобразуем строку для обработки четных и нечетных палиндромов
# # # #     # Например, "aba" -> "#a#b#a#", "abba" -> "#a#b#b#a#"
# # # #     processed_text = '#' + '#'.join(text) + '#'
# # # #     n = len(processed_text)
# # # #     P = [0] * n  # P[i] хранит радиус палиндрома с центром в i
# # # #     C = 0        # Центр текущего самого правого палиндрома
# # # #     R = 0        # Правая граница текущего самого правого палиндрома

# # # #     for i in range(n):
# # # #         # Находим зеркальное отражение i относительно C
# # # #         mirror_i = 2 * C - i

# # # #         # Если i внутри R, используем P[mirror_i]
# # # #         if i < R:
# # # #             P[i] = min(R - i, P[mirror_i])

# # # #         # Расширяем палиндром с центром в i
# # # #         a = i + (1 + P[i])
# # # #         b = i - (1 + P[i])
# # # #         while a < n and b >= 0 and processed_text[a] == processed_text[b]:
# # # #             P[i] += 1
# # # #             a += 1
# # # #             b -= 1

# # # #         # Обновляем C и R, если палиндром с центром в i расширяется дальше R
# # # #         if i + P[i] > R:
# # # #             C = i
# # # #             R = i + P[i]
    
# # # #     # Находим максимальный радиус и его центр
# # # #     max_len = 0
# # # #     center_index = 0
# # # #     for i in range(n):
# # # #         if P[i] > max_len:
# # # #             max_len = P[i]
# # # #             center_index = i
    
# # # #     # Восстанавливаем самую длинную палиндромную подстроку
# # # #     start_index = (center_index - max_len) // 2
# # # #     return text[start_index : start_index + max_len]

# # # # # Пример использования:
# # # # # print(manacher("babad")) # Выведет: "bab" или "aba"
# # # # # print(manacher("cbbd"))  # Выведет: "bb"


# # # # # Suffix Array (для эффективного поиска подстрок)
# # # # def build_suffix_array(text):
# # # #     n = len(text)
# # # #     suffixes = []
# # # #     for i in range(n):
# # # #         suffixes.append((text[i:], i))
    
# # # #     suffixes.sort() # Сортируем суффиксы лексикографически

# # # #     suffix_array = [s[1] for s in suffixes]
# # # #     return suffix_array

# # # # # Пример использования:
# # # # # text = "banana"
# # # # # suffix_arr = build_suffix_array(text)
# # # # # print(suffix_arr) # Выведет: [5, 3, 1, 0, 4, 2] (индексы: a, ana, anana, banana, na, nana)


# # # # # Segment Tree (Дерево отрезков) для запросов суммы диапазона
# # # # class SegmentTree:
# # # #     def __init__(self, arr):
# # # #         self.n = len(arr)
# # # #         self.tree = [0] * (4 * self.n) # Примерный размер дерева: 4*N
# # # #         self._build(arr, 0, 0, self.n - 1)

# # # #     def _build(self, arr, tree_index, lo, hi):
# # # #         if lo == hi:
# # # #             self.tree[tree_index] = arr[lo]
# # # #             return
# # # #         mid = (lo + hi) // 2
# # # #         self._build(arr, 2 * tree_index + 1, lo, mid)
# # # #         self._build(arr, 2 * tree_index + 2, mid + 1, hi)
# # # #         self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

# # # #     def query(self, query_lo, query_hi):
# # # #         return self._query(0, 0, self.n - 1, query_lo, query_hi)

# # # #     def _query(self, tree_index, lo, hi, query_lo, query_hi):
# # # #         # Полное перекрытие
# # # #         if query_lo <= lo and hi <= query_hi:
# # # #             return self.tree[tree_index]
        
# # # #         # Нет перекрытия
# # # #         if hi < query_lo or lo > query_hi:
# # # #             return 0
        
# # # #         # Частичное перекрытие
# # # #         mid = (lo + hi) // 2
# # # #         left_sum = self._query(2 * tree_index + 1, lo, mid, query_lo, query_hi)
# # # #         right_sum = self._query(2 * tree_index + 2, mid + 1, hi, query_lo, query_hi)
# # # #         return left_sum + right_sum

# # # #     def update(self, index, new_value):
# # # #         self._update(0, 0, self.n - 1, index, new_value)

# # # #     def _update(self, tree_index, lo, hi, index, new_value):
# # # #         if lo == hi:
# # # #             self.tree[tree_index] = new_value
# # # #             return
# # # #         mid = (lo + hi) // 2
# # # #         if lo <= index <= mid:
# # # #             self._update(2 * tree_index + 1, lo, mid, index, new_value)
# # # #         else:
# # # #             self._update(2 * tree_index + 2, mid + 1, hi, index, new_value)
# # # #         self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

# # # # # Пример использования:
# # # # # arr = [1, 3, 5, 7, 9, 11]
# # # # # st = SegmentTree(arr)
# # # # # print(st.query(1, 4)) # Выведет: 24 (3 + 5 + 7 + 9)
# # # # # st.update(2, 10)
# # # # # print(st.query(1, 4)) # Выведет: 29 (3 + 10 + 7 + 9)


# # # # Kuhn's Algorithm (для нахождения максимального паросочетания в двудольном графе)
# # # # (Простая реализация с использованием DFS)
# # # def find_matching(graph, u, visited, match_r):
# # #     for v in graph[u]:
# # #         if not visited[v]:
# # #             visited[v] = True
# # #             if match_r[v] == -1 or find_matching(graph, match_r[v], visited, match_r):
# # #                 match_r[v] = u
# # #                 return True
# # #     return False

# # # def max_bipartite_matching(graph):
# # #     num_left_vertices = len(graph)
# # #     # Предполагаем, что правые вершины нумеруются от 0 до max_v_index
# # #     # Найдем максимальный индекс правой вершины
# # #     max_v_index = -1
# # #     for u in graph:
# # #         for v in graph[u]:
# # #             max_v_index = max(max_v_index, v)
    
# # #     num_right_vertices = max_v_index + 1
# # #     match_r = [-1] * num_right_vertices # match_r[v] хранит вершину u, с которой v сопоставлена
# # #     result = 0

# # #     for u in range(num_left_vertices):
# # #         visited = [False] * num_right_vertices
# # #         if find_matching(graph, u, visited, match_r):
# # #             result += 1
# # #     return result

# # # # Пример использования:
# # # # graph = {
# # # #     0: [0, 1],
# # # #     1: [0],
# # # #     2: [0, 1]
# # # # }
# # # # print(max_bipartite_matching(graph)) # Выведет: 2


# # # # Tarjan's Algorithm (для нахождения сильно связных компонент (SCC))
# # # from collections import defaultdict

# # # class TarjanSCC:
# # #     def __init__(self, graph):
# # #         self.graph = graph
# # #         self.index = 0
# # #         self.stack = []
# # #         self.on_stack = defaultdict(bool)
# # #         self.ids = defaultdict(lambda: -1)
# # #         self.low_link = defaultdict(lambda: -1)
# # #         self.sccs = []
        
# # #         for node in graph:
# # #             if self.ids[node] == -1:
# # #                 self._dfs(node)

# # #     def _dfs(self, u):
# # #         self.ids[u] = self.index
# # #         self.low_link[u] = self.index
# # #         self.index += 1
# # #         self.stack.append(u)
# # #         self.on_stack[u] = True

# # #         for v in self.graph[u]:
# # #             if self.ids[v] == -1:
# # #                 self._dfs(v)
# # #                 self.low_link[u] = min(self.low_link[u], self.low_link[v])
# # #             elif self.on_stack[v]:
# # #                 self.low_link[u] = min(self.low_link[u], self.ids[v])
        
# # #         if self.ids[u] == self.low_link[u]:
# # #             current_scc = []
# # #             while True:
# # #                 node = self.stack.pop()
# # #                 self.on_stack[node] = False
# # #                 current_scc.append(node)
# # #                 if node == u:
# # #                     break
# # #             self.sccs.append(current_scc)

# # # # Пример использования:
# # # # graph = {
# # # #     0: [1],
# # # #     1: [2],
# # # #     2: [0],
# # # #     3: [1, 4],
# # # #     4: [3]
# # # # }
# # # # tarjan = TarjanSCC(graph)
# # # # print(tarjan.sccs) # Выведет: [[2, 1, 0], [4, 3]] (порядок может отличаться)


# # # # KMP Algorithm (Кнут-Моррис-Пратт) для поиска подстроки
# # # def compute_lps_array(pattern):
# # #     length = 0 # Длина предыдущего самого длинного префикса-суффикса
# # #     lps = [0] * len(pattern)
# # #     i = 1
# # #     while i < len(pattern):
# # #         if pattern[i] == pattern[length]:
# # #             length += 1
# # #             lps[i] = length
# # #             i += 1
# # #         else:
# # #             if length != 0:
# # #                 length = lps[length - 1]
# # #             else:
# # #                 lps[i] = 0
# # #                 i += 1
# # #     return lps

# # # def kmp_search(text, pattern):
# # #     n = len(text)
# # #     m = len(pattern)

# # #     lps = compute_lps_array(pattern)

# # #     i = 0 # индекс для text
# # #     j = 0 # индекс для pattern
# # #     occurrences = []

# # #     while i < n:
# # #         if pattern[j] == text[i]:
# # #             i += 1
# # #             j += 1
        
# # #         if j == m:
# # #             occurrences.append(i - j) # Найден шаблон
# # #             j = lps[j - 1]
# # #         elif i < n and pattern[j] != text[i]:
# # #             if j != 0:
# # #                 j = lps[j - 1]
# # #             else:
# # #                 i += 1
# # #     return occurrences

# # # # Пример использования:
# # # # text = "ABABDABACDABABCABAB"
# # # # pattern = "ABABCABAB"
# # # # print(kmp_search(text, pattern)) # Выведет: [10]


# # # # Euclidean Algorithm (Алгоритм Евклида для нахождения НОД)
# # # def gcd_euclidean(a, b):
# # #     while b:
# # #         a, b = b, a % b
# # #     return a

# # # # Пример использования:
# # # # print(gcd_euclidean(48, 18)) # Выведет: 6
# # # # print(gcd_euclidean(101, 103)) # Выведет: 1


# # # # Shell Sort (Сортировка Шелла)
# # # def shell_sort(arr):
# # #     n = len(arr)
# # #     gap = n // 2

# # #     while gap > 0:
# # #         for i in range(gap, n):
# # #             temp = arr[i]
# # #             j = i
# # #             while j >= gap and arr[j - gap] > temp:
# # #                 arr[j] = arr[j - gap]
# # #                 j -= gap
# # #             arr[j] = temp
# # #         gap //= 2
# # #     return arr

# # # # Пример использования:
# # # # arr = [12, 34, 54, 2, 3]
# # # # print(shell_sort(arr)) # Выведет: [2, 3, 12, 34, 54]


# # # # =================

# # # # Selection Sort (Сортировка выбором)
# # # def selection_sort(arr):
# # #     n = len(arr)
# # #     for i in range(n):
# # #         min_idx = i
# # #         for j in range(i + 1, n):
# # #             if arr[j] < arr[min_idx]:
# # #                 min_idx = j
# # #         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# # #     return arr

# # # # Пример использования:
# # # # arr = [64, 25, 12, 22, 11]
# # # # print(selection_sort(arr)) # Выведет: [11, 12, 22, 25, 64]

# # # # =================

# # # # Insertion Sort (Сортировка вставками)
# # # def insertion_sort(arr):
# # #     for i in range(1, len(arr)):
# # #         key = arr[i]
# # #         j = i - 1
# # #         while j >= 0 and key < arr[j]:
# # #             arr[j + 1] = arr[j]
# # #             j -= 1
# # #         arr[j + 1] = key
# # #     return arr

# # # # Пример использования:
# # # # arr = [12, 11, 13, 5, 6]
# # # # print(insertion_sort(arr)) # Выведет: [5, 6, 11, 12, 13]

# # # # =================

# # # # Counting Sort (Сортировка подсчётом)
# # # def counting_sort(arr):
# # #     if not arr:
# # #         return []

# # #     max_val = max(arr)
# # #     count = [0] * (max_val + 1)
    
# # #     for num in arr:
# # #         count[num] += 1
    
# # #     sorted_arr = []
# # #     for i in range(len(count)):
# # #         sorted_arr.extend([i] * count[i])
# # #     return sorted_arr

# # # # Пример использования:
# # # # arr = [4, 2, 2, 8, 3, 3, 1]
# # # # print(counting_sort(arr)) # Выведет: [1, 2, 2, 3, 3, 4, 8]

# # # # =================

# # # # Radix Sort (Поразрядная сортировка)
# # # def counting_sort_for_radix(arr, exp):
# # #     n = len(arr)
# # #     output = [0] * n
# # #     count = [0] * 10 # Для цифр от 0 до 9

# # #     for i in range(n):
# # #         index = arr[i] // exp
# # #         count[index % 10] += 1

# # #     for i in range(1, 10):
# # #         count[i] += count[i - 1]

# # #     i = n - 1
# # #     while i >= 0:
# # #         index = arr[i] // exp
# # #         output[count[index % 10] - 1] = arr[i]
# # #         count[index % 10] -= 1
# # #         i -= 1
    
# # #     for i in range(n):
# # #         arr[i] = output[i]

# # # def radix_sort(arr):
# # #     if not arr:
# # #         return []

# # #     max_val = max(arr)
# # #     exp = 1
# # #     while max_val // exp > 0:
# # #         counting_sort_for_radix(arr, exp)
# # #         exp *= 10
# # #     return arr

# # # # Пример использования:
# # # # arr = [170, 45, 75, 90, 802, 24, 2, 66]
# # # # print(radix_sort(arr)) # Выведет: [2, 24, 45, 66, 75, 90, 170, 802]

# # # # =================

# # # # Heap Sort (Пирамидальная сортировка)
# # # def heapify(arr, n, i):
# # #     largest = i
# # #     l = 2 * i + 1
# # #     r = 2 * i + 2

# # #     if l < n and arr[l] > arr[largest]:
# # #         largest = l
    
# # #     if r < n and arr[r] > arr[largest]:
# # #         largest = r
    
# # #     if largest != i:
# # #         arr[i], arr[largest] = arr[largest], arr[i]
# # #         heapify(arr, n, largest)

# # # def heap_sort(arr):
# # #     n = len(arr)

# # #     # Построение max-кучи
# # #     for i in range(n // 2 - 1, -1, -1):
# # #         heapify(arr, n, i)
    
# # #     # Извлечение элементов по одному
# # #     for i in range(n - 1, 0, -1):
# # #         arr[i], arr[0] = arr[0], arr[i] # Перемещаем текущий корень в конец
# # #         heapify(arr, i, 0)
# # #     return arr

# # # # Пример использования:
# # # # arr = [12, 11, 13, 5, 6, 7]
# # # # print(heap_sort(arr)) # Выведет: [5, 6, 7, 11, 12, 13]


# # # =================

# # # Boyer-Moore Algorithm (Алгоритм Бойера-Мура для поиска подстроки)
# # def build_bad_char_table(pattern):
# #     """Строит таблицу плохих символов для алгоритма Бойера-Мура"""
# #     table = {}
# #     for i in range(len(pattern) - 1):
# #         table[pattern[i]] = len(pattern) - 1 - i
# #     return table

# # def boyer_moore_search(text, pattern):
# #     """Поиск подстроки с помощью алгоритма Бойера-Мура"""
# #     if not pattern or not text:
# #         return []
    
# #     n, m = len(text), len(pattern)
# #     bad_char_table = build_bad_char_table(pattern)
# #     occurrences = []
    
# #     i = m - 1  # Индекс в тексте
# #     while i < n:
# #         j = m - 1  # Индекс в паттерне
# #         k = i      # Позиция в тексте для сравнения
        
# #         # Сравниваем паттерн справа налево
# #         while j >= 0 and text[k] == pattern[j]:
# #             k -= 1
# #             j -= 1
        
# #         if j == -1:  # Найден паттерн
# #             occurrences.append(k + 1)
# #             i += 1
# #         else:
# #             # Сдвиг на основе таблицы плохих символов
# #             bad_char_shift = bad_char_table.get(text[k], m)
# #             i += max(1, bad_char_shift - (m - 1 - j))
    
# #     return occurrences

# # # Пример использования:
# # # text = "AABAACAADAABAABA"
# # # pattern = "AABA"
# # # print(boyer_moore_search(text, pattern)) # Выведет: [0, 9, 12]


# # # =================

# # # Rabin-Karp Algorithm (Алгоритм Рабина-Карпа для поиска подстроки)
# # def rabin_karp_search(text, pattern, prime=101):
# #     """Поиск подстроки с помощью алгоритма Рабина-Карпа"""
# #     if not pattern or not text:
# #         return []
    
# #     n, m = len(text), len(pattern)
# #     occurrences = []
    
# #     # Вычисляем хеш паттерна
# #     pattern_hash = 0
# #     text_hash = 0
# #     h = 1
    
# #     # Вычисляем h = pow(prime, m-1) % prime
# #     for i in range(m - 1):
# #         h = (h * 256) % prime
    
# #     # Вычисляем хеш для паттерна и первого окна текста
# #     for i in range(m):
# #         pattern_hash = (256 * pattern_hash + ord(pattern[i])) % prime
# #         text_hash = (256 * text_hash + ord(text[i])) % prime
    
# #     # Скользим окно по тексту
# #     for i in range(n - m + 1):
# #         if pattern_hash == text_hash:
# #             # Проверяем символы, если хеши совпадают
# #             if text[i:i+m] == pattern:
# #                 occurrences.append(i)
        
# #         if i < n - m:
# #             # Вычисляем хеш для следующего окна
# #             text_hash = (256 * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
# #             if text_hash < 0:
# #                 text_hash += prime
    
# #     return occurrences

# # # Пример использования:
# # # text = "AABAACAADAABAABA"
# # # pattern = "AABA"
# # # print(rabin_karp_search(text, pattern)) # Выведет: [0, 9, 12]


# # # =================

# # # Fenwick Tree (Binary Indexed Tree) для запросов суммы диапазона
# # class FenwickTree:
# #     """Дерево Фенвика для эффективных запросов суммы диапазона"""
    
# #     def __init__(self, arr):
# #         self.n = len(arr)
# #         self.tree = [0] * (self.n + 1)
# #         self._build(arr)
    
# #     def _build(self, arr):
# #         """Построение дерева Фенвика"""
# #         for i in range(self.n):
# #             self.update(i, arr[i])
    
# #     def _get_lsb(self, x):
# #         """Получение младшего значащего бита"""
# #         return x & (-x)
    
# #     def update(self, index, value):
# #         """Обновление элемента по индексу"""
# #         index += 1  # Индексация с 1
# #         while index <= self.n:
# #             self.tree[index] += value
# #             index += self._get_lsb(index)
    
# #     def query(self, index):
# #         """Запрос суммы от 0 до index (включительно)"""
# #         index += 1  # Индексация с 1
# #         result = 0
# #         while index > 0:
# #             result += self.tree[index]
# #             index -= self._get_lsb(index)
# #         return result
    
# #     def range_query(self, left, right):
# #         """Запрос суммы в диапазоне [left, right]"""
# #         return self.query(right) - self.query(left - 1)

# # # Пример использования:
# # # arr = [1, 3, 5, 7, 9, 11]
# # # ft = FenwickTree(arr)
# # # print(ft.range_query(1, 4))  # Выведет: 24 (3 + 5 + 7 + 9)
# # # ft.update(2, 10)  # Увеличиваем элемент с индексом 2 на 10
# # # print(ft.range_query(1, 4))  # Выведет: 34 (3 + 15 + 7 + 9)


# # # =================

# # # Trie (Префиксное дерево) для эффективного поиска строк
# # class TrieNode:
# #     """Узел префиксного дерева"""
# #     def __init__(self):
# #         self.children = {}
# #         self.is_end_of_word = False
# #         self.word_count = 0

# # class Trie:
# #     """Префиксное дерево для эффективного поиска строк"""
    
# #     def __init__(self):
# #         self.root = TrieNode()
    
# #     def insert(self, word):
# #         """Вставка слова в дерево"""
# #         node = self.root
# #         for char in word:
# #             if char not in node.children:
# #                 node.children[char] = TrieNode()
# #             node = node.children[char]
# #             node.word_count += 1
# #         node.is_end_of_word = True
    
# #     def search(self, word):
# #         """Поиск точного совпадения слова"""
# #         node = self._get_node(word)
# #         return node is not None and node.is_end_of_word
    
# #     def starts_with(self, prefix):
# #         """Проверка, есть ли слова с данным префиксом"""
# #         return self._get_node(prefix) is not None
    
# #     def _get_node(self, word):
# #         """Получение узла для заданного слова"""
# #         node = self.root
# #         for char in word:
# #             if char not in node.children:
# #                 return None
# #             node = node.children[char]
# #         return node
    
# #     def count_words_with_prefix(self, prefix):
# #         """Подсчет слов с заданным префиксом"""
# #         node = self._get_node(prefix)
# #         return node.word_count if node else 0
    
# #     def get_all_words_with_prefix(self, prefix):
# #         """Получение всех слов с заданным префиксом"""
# #         node = self._get_node(prefix)
# #         if not node:
# #             return []
        
# #         words = []
# #         self._dfs_collect_words(node, prefix, words)
# #         return words
    
# #     def _dfs_collect_words(self, node, current_word, words):
# #         """DFS для сбора всех слов из поддерева"""
# #         if node.is_end_of_word:
# #             words.append(current_word)
        
# #         for char, child in node.children.items():
# #             self._dfs_collect_words(child, current_word + char, words)

# # # Пример использования:
# # # trie = Trie()
# # # words = ["apple", "app", "application", "banana", "band"]
# # # for word in words:
# # #     trie.insert(word)
# # # 
# # # print(trie.search("apple"))  # True
# # # print(trie.search("appl"))   # False
# # # print(trie.starts_with("app"))  # True
# # # print(trie.count_words_with_prefix("app"))  # 3
# # # print(trie.get_all_words_with_prefix("app"))  # ['app', 'apple', 'application']


# # # =================

# # # Union-Find (Disjoint Set Union) с ранжированием и сжатием путей
# # class UnionFind:
# #     """Структура данных Union-Find с оптимизациями"""
    
# #     def __init__(self, n):
# #         """Инициализация с n элементами"""
# #         self.parent = list(range(n))
# #         self.rank = [0] * n
# #         self.size = [1] * n  # Размер каждого множества
# #         self.count = n       # Количество множеств
    
# #     def find(self, x):
# #         """Поиск корня элемента с сжатием путей"""
# #         if self.parent[x] != x:
# #             self.parent[x] = self.find(self.parent[x])
# #         return self.parent[x]
    
# #     def union(self, x, y):
# #         """Объединение множеств с ранжированием"""
# #         root_x = self.find(x)
# #         root_y = self.find(y)
        
# #         if root_x == root_y:
# #             return False  # Уже в одном множестве
        
# #         # Объединяем по рангу
# #         if self.rank[root_x] < self.rank[root_y]:
# #             root_x, root_y = root_y, root_x
        
# #         self.parent[root_y] = root_x
# #         self.size[root_x] += self.size[root_y]
        
# #         if self.rank[root_x] == self.rank[root_y]:
# #             self.rank[root_x] += 1
        
# #         self.count -= 1
# #         return True
    
# #     def connected(self, x, y):
# #         """Проверка, находятся ли элементы в одном множестве"""
# #         return self.find(x) == self.find(y)
    
# #     def get_size(self, x):
# #         """Получение размера множества, содержащего элемент x"""
# #         root = self.find(x)
# #         return self.size[root]
    
# #     def get_count(self):
# #         """Получение количества множеств"""
# #         return self.count
    
# #     def get_components(self):
# #         """Получение всех компонент"""
# #         components = {}
# #         for i in range(len(self.parent)):
# #             root = self.find(i)
# #             if root not in components:
# #                 components[root] = []

# # =================

# # 1. Дейкстра с восстановлением пути
# import heapq

# def dijkstra_with_path(graph, start):
#     """Дейкстра с восстановлением кратчайших путей"""
#     distances = {node: float('inf') for node in graph}
#     previous = {node: None for node in graph}
#     distances[start] = 0
#     queue = [(0, start)]
#     while queue:
#         dist, u = heapq.heappop(queue)
#         if dist > distances[u]:
#             continue
#         for v, weight in graph[u].items():
#             if distances[v] > distances[u] + weight:
#                 distances[v] = distances[u] + weight
#                 previous[v] = u
#                 heapq.heappush(queue, (distances[v], v))
#     return distances, previous

# def restore_path(previous, start, end):
#     """Восстановление пути из previous"""
#     path = []
#     while end is not None:
#         path.append(end)
#         end = previous[end]
#     path.reverse()
#     if path and path[0] == start:
#         return path
#     return []

# # Пример использования:
# # graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
# # dist, prev = dijkstra_with_path(graph, 'A')
# # print(dist)
# # print(restore_path(prev, 'A', 'D'))

# # =================

# # 2. Поиск мостов (Tarjan's Bridge Algorithm)
# def find_bridges(graph):
#     """Поиск мостов в неориентированном графе"""
#     bridges = []
#     time = [0]
#     visited = set()
#     tin = {}
#     low = {}
#     def dfs(u, parent):
#         visited.add(u)
#         tin[u] = low[u] = time[0]
#         time[0] += 1
#         for v in graph[u]:
#             if v == parent:
#                 continue
#             if v in visited:
#                 low[u] = min(low[u], tin[v])
#             else:
#                 dfs(v, u)
#                 low[u] = min(low[u], low[v])
#                 if low[v] > tin[u]:
#                     bridges.append((u, v))
#     for u in graph:
#         if u not in visited:
#             dfs(u, None)
#     return bridges

# # Пример использования:
# # graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
# # print(find_bridges(graph)) # [(3, 4), (2, 3)]

# # =================

# # 3. Поиск точек сочленения (articulation points)
# def find_articulation_points(graph):
#     """Поиск точек сочленения в неориентированном графе"""
#     points = set()
#     time = [0]
#     visited = set()
#     tin = {}
#     low = {}
#     def dfs(u, parent=None):
#         visited.add(u)
#         tin[u] = low[u] = time[0]
#         time[0] += 1
#         children = 0
#         for v in graph[u]:
#             if v == parent:
#                 continue
#             if v in visited:
#                 low[u] = min(low[u], tin[v])
#             else:
#                 dfs(v, u)
#                 low[u] = min(low[u], low[v])
#                 if parent is not None and low[v] >= tin[u]:
#                     points.add(u)
#                 children += 1
#         if parent is None and children > 1:
#             points.add(u)
#     for u in graph:
#         if u not in visited:
#             dfs(u)
#     return points

# # Пример использования:
# # graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
# # print(find_articulation_points(graph)) # {2, 3}

# # =================

# # 4. Edmonds-Karp (максимальный поток)
# from collections import deque, defaultdict

# def edmonds_karp(capacity, source, sink):
#     """Поиск максимального потока в графе (Edmonds-Karp)"""
#     n = len(capacity)
#     flow = 0
#     parent = {}
#     def bfs():
#         visited = set()
#         queue = deque([source])
#         visited.add(source)
#         parent.clear()
#         while queue:
#             u = queue.popleft()
#             for v in capacity[u]:
#                 if v not in visited and capacity[u][v] > 0:
#                     visited.add(v)
#                     parent[v] = u
#                     if v == sink:
#                         return True
#                     queue.append(v)
#         return False
#     while bfs():
#         path_flow = float('inf')
#         s = sink
#         while s != source:
#             path_flow = min(path_flow, capacity[parent[s]][s])
#             s = parent[s]
#         v = sink
#         while v != source:
#             u = parent[v]
#             capacity[u][v] -= path_flow
#             capacity[v].setdefault(u, 0)
#             capacity[v][u] += path_flow
#             v = parent[v]
#         flow += path_flow
#     return flow

# # Пример использования:
# # capacity = {0: {1: 16, 2: 13}, 1: {2: 10, 3: 12}, 2: {1: 4, 4: 14}, 3: {2: 9, 5: 20}, 4: {3: 7, 5: 4}, 5: {}}
# # print(edmonds_karp(capacity, 0, 5)) # 23

# # =================

# # 5. Минимальное покрытие вершин в двудольном графе через максимальное паросочетание
# # (König's theorem)
# def min_vertex_cover_bipartite(graph, left_size):
#     """Минимальное покрытие вершин в двудольном графе через максимальное паросочетание"""
#     # graph: {u: [v, ...]} где u из левой доли, v из правой (номера)
#     match_to = [-1] * (max(max(vs) for vs in graph.values()) + 1)
#     def bpm(u, visited):
#         for v in graph[u]:
#             if not visited[v]:
#                 visited[v] = True
#                 if match_to[v] == -1 or bpm(match_to[v], visited):
#                     match_to[v] = u
#                     return True
#         return False
#     for u in range(left_size):
#         visited = [False] * len(match_to)
#         bpm(u, visited)
#     # Теперь строим минимальное покрытие
#     from collections import deque
#     vis_left = [False] * left_size
#     vis_right = [False] * len(match_to)
#     queue = deque()
#     for u in range(left_size):
#         if all(match_to[v] != u for v in graph[u]):
#             queue.append(u)
#             vis_left[u] = True
#     while queue:
#         u = queue.popleft()
#         for v in graph[u]:
#             if not vis_right[v] and match_to[v] != -1 and match_to[v] != u:
#                 vis_right[v] = True
#                 if not vis_left[match_to[v]]:
#                     vis_left[match_to[v]] = True
#                     queue.append(match_to[v])
#     cover_left = [u for u in range(left_size) if not vis_left[u]]
#     cover_right = [v for v in range(len(match_to)) if vis_right[v]]
#     return cover_left, cover_right

# # Пример использования:
# # graph = {0: [0, 1], 1: [0], 2: [1]}
# # left_size = 3
# # print(min_vertex_cover_bipartite(graph, left_size)) # ([1, 2], [0])
