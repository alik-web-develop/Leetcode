# ?///////////////////////////////// TASK №1 /////////////
# x = "hello world it's new ^^ * text) (( "
# def one_word(x):
#     uniq_symbl = []
#     for i in x:
#         idx = x.index(i)
#         r = x[idx+1:len(x)]
#         if i not in r:
#             uniq_symbl += i
#     return uniq_symbl
# print(one_word(x))
# ?///////////////////////////////// TASK №2 /////////////
# x = int(input("give id length "))
# def create_id(id_len):
#     import random
#     result = ""
#     symbols = "!@#$%^&*()_+?><}{?~}qwertyuiopasdfghjklzxcvbnm1234567890"
#     for i in range(id_len):
#         num = random.randint(0,len(symbols))
#         result += symbols[num]
#     return result
# print("your id this: " + create_id(x))
# ?///////////////////////////////// TASK №3 /////////////
# x = "hello world this is test text"
# def all_caps(words):
#     result = ""
#     for i in words.split():
#         result += f"{i[0].upper()}{i[1:len(i)]} "
#     return result
# print(all_caps(x))
# ?///////////////////////////////// TASK №4 /////////////
# x = ["hello world","this is new text","new text","test text"]
# def all_caps(words):
#     result = []
#     for i in words:
#         result.append(i[::-1])
#     return result
# print(all_caps(x))
# ?///////////////////////////////// TASK №5 /////////////
# x = ["hola","world","this is text","new"]
# def sort_len_word(words):
#     return sorted(words,key=len)
# print(sort_len_word(x))
# ?///////////////////////////////// TASK №6 /////////////
# x = "hello world this is new test text aaaaaaa f"
# def lot_time_letter(words):
#     set_words = ''.join(set(words.replace(" ","")))
#     result = {i: 0 for i in set_words}
#     for i in words:
#         if i in result:
#             result[i] += 1
#     return sorted(result.items(),key=lambda item: item[1])[len(set_words)-1]
    
# print(lot_time_letter(x))
# ?///////////////////////////////// TASK №7 /////////////
# x = "hello world this is new test text"
# def next_vowel(words):
#     result = ""
#     for i in words:
#         if i == "a":
#             result += "e"
#         elif i == "e":
#             result += "i"
#         elif i == "i":
#             result += "o"
#         elif i == "o":
#             result += "u"
#         else:
#             result += i
#     return result
# print(next_vowel(x))

# x = [1,1,2]
# def removeDuplicates(nums):
#     result = []
#     symbols = []
#     for i in nums:
#         if i not in result:
#             result.append(i)
#         else:
#             symbols += "_"
#     return result + symbols
# print(removeDuplicates(x))f


# numbers = [12,34,62,7,12,523,96,423,89]

# def odd_max_num(item):
#     if item % 2 != 0:
#         return item
#     else:
#         return 1
# print(min(numbers, key=odd_max_num))

# text = "new neeww nwwww"
# def func(item):
#     v_count = [i for i in item if i.lower() in "w"]
#     return len(v_count)
# print(max(text.split(" "), key=func))

# text = "Hello world this is new world"
# # def func(item):
# #     v_count = "".join([i for i in item if i.lower() in "aeiou"])
# #     return v_count
# # result = " ".join(list(map(func,text.split(" "))))
# # print(result)


# cars_for_user = [
#         {"name":"BMW", "price":10000},
#         {"name":"Mercedes", "price":15000},
#         {"name":"Audi", "price":20000},
#         {"name":"Volkswagen", "price":12000},
#         {"name":"Toyota", "price":18000},
#         {"name":"Ford", "price":13000}
#     ]
# def func(item):
#     item["salary"] = 800
#     item["month"] = item["price"] / item["salary"]
#     return item
# result = list(map(func,cars_for_user))
# [print(i) for i in result]





# from functools import reduce 
# l = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda item:True if item % 2 == 0 else False,l))
# result = reduce(lambda acc,next: acc + next, evens)
# print(result)


from functools import reduce
# numbers = [1,5,"43",7,"90","a","f"]
# def func(acc,next):
#     if str(next).isnumeric():
#         return acc + int(next)
#     else:
#         return acc
# sum_list = reduce(func,numbers) 
# print(sum_list)

text = "hello world this is new text"
def func(acc,next):
    
symbols_in_text = reduce(func,text,{'':0,"original_text":text})
print(symbols_in_text)


    