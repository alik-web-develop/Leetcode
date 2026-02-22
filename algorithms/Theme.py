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

# # # # # # # # Пример исn range(2, int(n ** 0.5) + 1):
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
# # # #         mirr