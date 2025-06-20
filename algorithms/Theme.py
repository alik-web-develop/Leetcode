# # # # l = ["Hello", "abc","test","a","ab","world"]

# # # # def bubble_sort(u_ns):
# # # #     sorted = False
# # # #     while not sorted:
# # # #         sorted = True
# # # #         for i in range(len(u_ns)-1):
# # # #             if len(u_ns[i]) > len(u_ns[i+1]):
# # # #                 u_ns[i], u_ns[i + 1] = u_ns[i+1], u_ns[i]
# # # #                 sorted = False

# # # # bubble_sort(l)
# # # # print(l)
# # # # def pyr(num,num2=1):
# # # #     print(" "*num2 + "*"*(num-num2))
# # # #     if num > num2:
# # # #         return pyr(num-1,num2+1)
# # # #     else:
# # # #         return ""
# # # # pyr(10)

# # # def factorial(n):
# # #     if n == 0 or n == 1:
# # #         return 1
# # #     return n * factorial(n-1)

# # # # Пример использования:
# # # # print(factorial(5))  # Выведет: 120

# # # def is_prime(n):
# # #     if n < 2:
# # #         return False
# # #     for i in range(2, int(n ** 0.5) + 1):
# # #         if n % i == 0:
# # #             return False
# # #     return True

# # # # Пример использования:
# # # # print(is_prime(17))  # Выведет: True
# # # # print(is_prime(20))  # Выведет: False

# # # def fibonacci(n):
# # #     if n <= 0:
# # #         return []
# # #     elif n == 1:
# # #         return [0]
# # #     fib = [0, 1]
# # #     for i in range(2, n):
# # #         fib.append(fib[i-1] + fib[i-2])
# # #     return fib

# # # # Пример использования:
# # # # print(fibonacci(10))  # Выведет: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# # # def is_palindrome(s):
# # #     # Удаляем пробелы и приводим к нижнему регистру
# # #     s = ''.join(c.lower() for c in s if c.isalnum())
# # #     return s == s[::-1]

# # # # Пример использования:
# # # # print(is_palindrome("A man, a plan, a canal: Panama"))  # Выведет: True
# # # # print(is_palindrome("hello"))  # Выведет: False

# # # def gcd(a, b):
# # #     while b:
# # #         a, b = b, a % b
# # #     return a

# # # # Пример использования:
# # # # print(gcd(48, 18))  # Выведет: 6
# # # # print(gcd(54, 24))  # Выведет: 6

# # # def two_sum(nums, target):
# # #     lookup = {}
# # #     for i, num in enumerate(nums):
# # #         if target - num in lookup:
# # #             return [lookup[target - num], i]
# # #         lookup[num] = i
# # #     return []

# # # # Пример использования:
# # # # print(two_sum([2, 7, 11, 15], 9))  # Выведет: [0, 1]

# class Bank:
#     def __init__(self, bank_name: str, account_id: int, pin: int):
#         self._bank_name = bank_name
#         self._bank_id = account_id
#         self._pin = pin
#         self._balance = 0

#     def __str__(self):
#         return f"You have a account on this bank- '{self._bank_name}'"

#     def print_msg(self, msg):
#         print("\n")
#         print("*" * 20)
#         print(msg)
#         print("*" * 20)
#         print("\n")

#     def validate_account_exist(self, account_id, pin) -> bool:
#         if self._bank_id == account_id and self._pin == pin:
#             return True
#         self.print_msg(f"No account exist on id {account_id}")
#         return False

#     def invest(self, amount: float, account_id: int, pin: int) -> bool:
#         """Вклад в личный счет"""
#         if self.validate_account_exist(account_id, pin):
#             self._balance = self._balance + amount
#             self.print_msg(
#                 f" SUCCESFULT INVEST your new balance {self._balance}")
#             return True
#         return False

#     def withdraw(self, amount: float, account_id: int, pin: int) -> bool:
#         if self.validate_account_exist(account_id, pin):
#             self._balance = self._balance - amount
#             self.print_msg(
#                 f" SUCCESLUFY WITHDRAW your new balance {self._balance}")
#             return True


# class HamkorBank(Bank):
#     def __init__(self, bank_name: str, account_id: int, pin: int, location: str):
#         super().__init__(bank_name, account_id, pin)
#         self.location = location


# account_id = 123908  # int!


