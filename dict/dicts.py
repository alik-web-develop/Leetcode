# ////////////task1
# x = {
#     "two": 2,
#     "fist": 1,
#     "three": 3
# }


# def sort_of_values(obj):
#     arr = list(obj.items())
#     for n in range(len(arr) - 1, 0, -1):
#         for i in range(n):
#             if arr[i][1] > arr[i + 1][1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr


# print(sort_of_values(x))
# ............task2
# x = {0: 10, 1: 20}
# def continue_dict(obj):
#     max_key = max(obj.keys())
#     obj[max_key + 1] = (max_key * 10) + 10
#     return obj
# print(continue_dict(x))
# ............task3
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={7:70,8:80}
# def merge(*args):
#     result = {}
#     for i in args:
#         result.update(i)
#     return result
# print(merge(dic1,dic2,dic3,dic4))
# ............task4

# x = {0: 10, 1: 20}
# def does_key_exist(obj,ex_key):
#     result = obj.pop(ex_key, False)
#     return f"this item was found this is its meaning: {result}" if result else "no such element was found"
# print(does_key_exist(x,0))
# ............task5
# x = {0: 10, 1: 20, 2: 30, 3: 40}
# def make_dict(obj):
#     return {key*key for key, val in obj.items()}
# print(make_dict(x))

# ............task6
# def dict_range(number):
#     result = {}
#     for i in range(1,number+1):
#         result[i] = i*i
#     return result
# print(dict_range(5))
# ............task7
# Алишер ака тут 6 и 7 задание одинаковые можете сами посмотреть я не стал просто число менять
# ............task8
# dic1 = {
#     1: "first",
#     2: "second",
#     3: "third",
#     4: "fourth",
#     5: "fifth"
# }
# dic2 = {
#     6: "sixth",
#     7: "seventh",
#     8: "eighth",
#     9: "ninth",
#     10: "tenth"
# }
# def merge(obj1,obj2):
#     result = {**obj1,**obj2}
#     return result
# print(merge(dic1,dic2))
# ............task9
# dic1 = {
#     1: 10,
#     2: 20,
#     3: 30,
#     4: 40,
#     5: 50
# }
# def all_sum_of_dict(obj):
#     return sum({val for _,val in obj.items() })
# print(all_sum_of_dict(dic1))

# ............task11
# dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# def all_multiplication_dictionary(obj):
#     result = 1
#     for i in obj.values():
#         result = i*result
#     return result

# print(all_multiplication_dictionary(dic1))

# ............task12

# dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# def del_key(obj):
#     first = next(iter(obj.keys()))
#     del obj[first]
#     return obj
# print(del_key(dic1))
# ............task13
# dic1 = {
#         1: 10,
#         4: 40,
#         5: 50,
#         2: 20,
#         3: 30,
#         }
# def smllst_bggst_val(obj):
#     biggest = 0
#     smallest = next(iter(obj.values()))
#     for _, val in obj.items():
#         if val > biggest:
#             biggest = val
#         if smallest > val:
#             smallest = val
#     return f"this is smallest num: {smallest} \n and this is bigsest :{biggest}"
# print(smllst_bggst_val(dic1))

# ............task14
# x = ["first","second","third"]
# y = [1,2,3]
# def merge(obj1,obj2):
#     return dict(zip(obj1,obj2))
# print(merge(x,y))
# ............task15
# def no_repeats(arr):
#     result = []
#     for i in arr:
#         if i not in result:
#             result.append(i)
#     return result
# z = {'first': 1, 'second': 2, 'third': 3,"third":3}
# def no_repetitions_dict(obj):
#     x = no_repeats(list(obj.values()))
#     y = no_repeats(list(obj.keys()))
#     return dict(zip(y,x))
# print(no_repetitions_dict(z))
# Алишер ака я тут мог сделать всё в одной функции но внутри функции было бы не очень акуратно так я побоялся сделать в одной функции потаму что вы сказали бы Clean Coding
# ............task19
# x = {"a":100,"b":200,"d":300,"c":400,"f":700,"g":1000}
# y = {"a":200,"b":300,"d":400,"c":500,"f":800,"g":-7}
# def two_val_sum(obj1,obj2):
#     result = list(zip(obj1.values(),obj2.values()))
#     main = []
#     [main.append(sum(list(i))) for i in result]
#     return dict(zip(obj1.keys(),main))
# print(two_val_sum(x,y))
# ладно это было сложно признаю но я сделал :) и я лучше самого себя вчерашнего, поетому смог

# ............task24
# x = "w3resource"
# def search_letter(word:str,letter:str):
#     return sum([len(i) for i in word if i == letter])
# def number_characters_in_value(word:str):
#     result = {}
#     for i in word:
#         result[i] = search_letter(word,i)
#     return result
# print(number_characters_in_value(x)) # {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# ............task22
# ............task22
# x = {'a':123,'b':5678,'c':765,'d':908,'e':89,'f':898,'g':1098,'s':9000}
# def highest_three_value(obj):
#     result = []
#     for i in obj.items():
#         result.append(i[1])
#     return sorted(result)[-3:len(result)]
# print(highest_three_value(x))
# ............task30

# x = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}


# def sort_of_values(obj):
#     arr = list(obj.items())
#     for n in range(len(arr) - 1, 0, -1):
#         for i in range(n):
#             if arr[i][1] > arr[i + 1][1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr[-3:len(arr)]


# print(sort_of_values(x))

# ............task31