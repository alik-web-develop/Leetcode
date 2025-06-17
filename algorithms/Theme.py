# # l = ["Hello", "abc","test","a","ab","world"]

# # def bubble_sort(u_ns):
# #     sorted = False
# #     while not sorted:
# #         sorted = True
# #         for i in range(len(u_ns)-1):
# #             if len(u_ns[i]) > len(u_ns[i+1]):
# #                 u_ns[i], u_ns[i + 1] = u_ns[i+1], u_ns[i]
# #                 sorted = False

# # bubble_sort(l)
# # print(l) 
# # def pyr(num,num2=1):
# #     print(" "*num2 + "*"*(num-num2))
# #     if num > num2:
# #         return pyr(num-1,num2+1)
# #     else:
# #         return ""
# # pyr(10)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# # Пример использования:
# # print(factorial(5))  # Выведет: 120

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

