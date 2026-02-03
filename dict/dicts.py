# # ////////////task1
# # x = {
# #     "two": 2,
# #     "fist": 1,
# #     "three": 3
# # }


# #             if arr[i][1] > arr[i + 1][1]:
# #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# #     return arr
# # print(sort_of_values(x))
# # ............task2
# # x = {0: 10, 1: 20}
# # def continue_dict(obj):
# #     max_key = max(obj.keys())
# #     obj[max_key + 1] = (max_key * 10) + 10
# #     re
# # x = {0: 10, 1: 20, 2: 30, 3: 40}
# # def make_dict(obj):
# #     return {key*key for key, val in obj.items()}
# # print(make_dict(x))

# # ............task6
# # def dict_range(number):
# #     return result
# # print(dict_range(5))
# # ............task7
# # Алишер ака тут 6 и 7 задание одинаковые можете сами посмотреть я не стал просто число менять
# # ............task8
# # dic1 = {
# # print(all_sum_of_dict(dic1))

# # ............task11
# # dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# # def all_multiplication_dictionary(obj):
# #     result = 1
# #     for i in obj.values():
# #         result = i*result
# #     return result

# # print(all_multiplication_dictionary(dic1))

# # ............task12

# # dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# # def del_key(obj):
# #     first = next(iter(obj.keys()))
# #     del obj[first]
# #     return obj
# # print(del_key(dic1))
# # ............task13
# # dic1 = {
# #         1: 10,
# #         4: 40,
# #         5: 50,
# #         2: 20,
# #         3: 30,
# #         }
# # def smllst_bggst_val(obj):
# #     biggest = 0
# #     smallest = next(iter(obj.values()))
# #     for _, val in obj.items():
# #         if val > biggest:
# #             biggest = val
# #         if smallest > val:
# #             smallest = val
# #     return f"this is smallest num: {smallest} \n and this is bigsest :{biggest}"
# # print(smllst_bggst_val(dic1))

# # ............task14
# # x = ["first","second","third"]
# # y = [1,2,3]
# # def merge(obj1,obj2):
# #     return dict(zip(obj1,obj2))
# # print(merge(x,y))
# # ............task15
# # def no_repeats(arr):
# #     result = []
# #     for i in arr:
# #         if i not in result:
# #             result.append(i)
# #     return result
# # z = {'first': 1, 'second': 2, 'third': 3,"third":3}
# # def no_repetitions_dict(obj):
# #     x = no_repeats(list(obj.values()))
# #     y = no_repeats(list(obj.keys()))
# #     return dict(zip(y,x))
# # print(no_repetitions_dict(z))
# # Алишер ака я тут мог сделать всё в одной функции но внутри функции было бы не очень акуратно так я побоялся сделать в одной функции потаму что вы сказали бы Clean Coding
# # ............task19
# # x = {"a":100,"b":200,"d":300,"c":400,"f":700,"g":1000}
# # y = {"a":200,"b":300,"d":400,"c":500,"f":800,"g":-7}
# # def two_val_sum(obj1,obj2):
# #     result = list(zip(obj1.values(),obj2.values()))
# #     main = []
# #     [main.append(sum(list(i))) for i in result]
# #     return dict(zip(obj1.keys(),main))
# # print(two_val_sum(x,y))
# # ладно это было сложно признаю но я сделал :) и я лучше самого себя вчерашнего, поетому смог

# # ............task24
# # x = "w3resource"
# # def search_letter(word:str,letter:str):
# #     return sum([len(i) for i in word if i == letter])
# # def number_characters_in_value(word:str):
# #     result = {}
# #     for i in word:
# #         result[i] = search_letter(word,i)
# #     return result
# # print(number_characters_in_value(x)) # {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# # ............task22
# # ............task22
# # x = {'a':123,'b':5678,'c':765,'d':908,'e':89,'f':898,'g':1098,'s':9000}
# # def highest_three_value(obj):
# #     result = []
# #     for i in obj.items():
# #         result.append(i[1])
# #     return sorted(result)[-3:len(result)]
# # print(highest_three_value(x))
# # ............task30

# # x = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}


# # def sort_of_values(obj):
# #     arr = list(obj.items())
# #     for n in range(len(arr) - 1, 0, -1):
# #         for i in range(n):
# #             if arr[i][1] > arr[i + 1][1]:
# #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# #     return arr[-3:len(arr)]


# # print(sort_of_values(x))
# # ............task38
# # x = {'key1': 1, 'key2': 3, 'key3': 2, 'key9': 9}
# # y = {'key1': 1, 'key2': 2, 'key9': 9}


# # def search_identical_objects(obj1, obj2):
# #     result = {}
# #     for key1, val1 in obj1.items():
# #         for key2, val2 in obj2.items():
# #             if key1 == key2 and val1 == val2:
# #                 result[key1] = val1
# #     return result


# # print(search_identical_objects(x, y))


# # ............task41
# # x = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# # def del_falses_in_dict(obj):
# #     result = {}
# #     for key,val in obj.items():
# #         if val and key:
# #             result[key] = val
# #     return result
# # print(del_falses_in_dict(x))

# # ............task42
# # x = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}


# # def allow_from_rating(obj, number):
# #     result = {key: val for key, val in obj.items() if val >= number}
# #     return result


# # print(allow_from_rating(x, 170))

# # ............task43
# # x = ['S001', 'S002', 'S003', 'S004']
# # y = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# # z = [85, 98, 89, 92]


# # def combine_information_by_details(tags, names, ratings):
# #     result = {}
# #     counter = 0
# #     for key, val in dict(zip(names, ratings)).items():
# #         result[tags[counter]] = {key: val}
# #         counter += 1
# #     return result

# # print(combine_information_by_details(x, y, z))

# # ............task44
# # x = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# # def filtration_for_physique(students,height,weight):
# #     result = {}
# #     for key,val in students.items():
# #         if val[0] >= height and val[1] >= weight:
# #             result[key] = val
# #     return result
# # print(filtration_for_physique(x,6,70))
# # ............task45
# # x = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# # def all_value_same(obj):
# #     return len(set([val for key,val in obj.items()])) == 1
# # print(all_value_same(x))
# # ............task46
# # x = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1),('red', 7)]
# # def group_identical_elements(dic):
# #     obj = {i[0]: []    for i in dic}
# #     for i in x:
# #         for key,val in obj.items():
# #             if key == i[0]:
# #                 val.append(i[1])
# #     return obj
# # print(group_identical_elements(x))
# # ............task47
# # x = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # def split_dict(obj):
# #     obj_keys = [i for i in obj.keys()]
# #     obj_vals = [i for i in obj.values()]
# #     result = []
# #     for i in range(len(obj_vals[1])):
# #         result.append({obj_keys[0]:obj_vals[0][i],obj_keys[1]:obj_vals[1][i]})
# #     return result
# # print(split_dict(x))
# # ............task48
# # x = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# # def del_element_in_dict(obj,element):
# #     result = []
# #     for i in x:
# #         if i['id'] != element:
# #             result.append(i)
# #     return result
# # print(del_element_in_dict(x,'#800000'))
# # ............task49
# # x = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99','l':'50'}]
# # def str_to_int_in_dict(obj):
# #     for y in x:
# #         for key, val in y.items():
# #             try:
# #                 y[key] = int(val)
# #             except ValueError:
# #                 y[key] = float(val)
# #     return obj


# # print(str_to_int_in_dict(x))

# # ............task50
# # x = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# # def clear_values(obj):
# #     return {key:[] for key,_ in obj.items()}
# # print(clear_values(x))
# # ............task51
# # x = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93],'hello World': [943,3,123]}
# # x.update({'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]})
# # print(x)
# # ............task52
# # x = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# # def find_value_by_keys(obj,find_key):
# #     result = []
# #     {result.append(i) for i in obj}
# #     return result
# # print(find_value_by_keys(x,'Science'))
# # ............task53
# # my_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# # def value_len(obj):
# #     return {val:len(val) for key,val in obj.items()}
# # print(value_len(my_dict))
# # ............task56
# # x = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# # def dict_to_list(obj):
# #     return [[key,val] for key,val in obj.items()]
# # print(dict_to_list(x))
# # ............task57
# # x = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# # def even_values_in_dict(obj):
# #     result = {}
# #     for key,val in obj.items():
# #         result[key] = [i for i in val if i % 2 == 0]
# #     return result
# # print(even_values_in_dict(x))
# # ............task59
# # x = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24,
# #      'f': 100, 'g': 57, 'h': 8, 'i': 100}


# # def sort_of_values(obj, number):
# #     arr = list(obj.items())
# #     for n in range(len(arr) - 1, 0, -1):
# #         for i in range(n):
# #             if arr[i][1] > arr[i + 1][1]:
# #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# #     return [i[0] for i in arr[-number:len(arr)]]


# # print(sort_of_values(x, 5))

# # ............task60

# # Задача: Найти все возможные комбинации ключей и значений
# def find_key_value_combinations(dict1, dict2):
#     result = []
#     for k1, v1 in dict1.items():
#         for k2, v2 in dict2.items():
#             result.append({k1: v1, k2: v2})
#     return result

# # Задача: Создать вложенный словарь из плоского
# def create_nested_dict(flat_dict, separator='_'):
#     result = {}
#     for key, value in flat_dict.items():
#         parts = key.split(separator)
#         current = result
#         for part in parts[:-1]:
#             if part not in current:
#                 current[part] = {}
#             current = current[part]
#         current[parts[-1]] = value
#     return result

# # Задача: Найти все пути в словаре
# def find_all_paths(dict_obj, path=None):
#     if path is None:
#         path = []
#     result = []
#     for key, value in dict_obj.items():
#         current_path = path + [key]
#         if isinstance(value, dict):
#             result.extend(find_all_paths(value, current_path))
#         else:
#             result.append(current_path)
#     return result

# # Задача: Объединить словари с учетом вложенности
# def deep_merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#         if key in result and isinstance(result[key], dict) and isinstance(value, dict):
#             result[key] = deep_merge_dicts(result[key], value)
#         else:
#             result[key] = value
#     return result
# # ............task63
# def find_dict_intersections(dict1, dict2):
#     """
#     Находит пересечения между двумя словарями по ключам и значениям.
    
#     Args:
#         dict1 (dict): Первый словарь
#         dict2 (dict): Второй словарь
        
#     Returns:
#         dict: Словарь с результатами пересечений, содержащий:
#             - common_keys: список общих ключей
#             - common_values: список общих значений
#             - common_key_value_pairs: список пар (ключ, значение), которые совпадают в обоих словарях
#     """
#     # Находим общие ключи
#     common_keys = list(set(dict1.keys()) & set(dict2.keys()))
    
#     # Находим общие значения
#     common_values = list(set(dict1.values()) & set(dict2.values()))
    
#     # Находим пары ключ-значение, которые совпадают в обоих словарях
#     common_pairs = [(key, dict1[key]) for key in common_keys if dict1[key] == dict2[key]]
    
#     return {
#         'common_keys': common_keys,
#         'common_values': common_values,
#         'common_key_value_pairs': common_pairs
#     }

# # Примеры использования:
# if __name__ == "__main__":
#     # Пример для find_key_value_combinations
#     dict1 = {'a': 1, 'b': 2}
#     dict2 = {'x': 10, 'y': 20}
#     print("Комбинации ключей и значений:")
#     print(find_key_value_combinations(dict1, dict2))
    
#     # Пример для create_nested_dict
#     flat_dict = {'a_b_c': 1, 'a_b_d': 2, 'x_y': 3}
#     print("\nВложенный словарь:")
#     print(create_nested_dict(flat_dict))
    
#     # Пример для find_all_paths
#     nested_dict = {'a': {'b': {'c': 1}, 'd': 2}, 'x': {'y': 3}}
#     print("\nВсе пути в словаре:")
#     print(find_all_paths(nested_dict))
    
#     # Пример для deep_merge_dicts
#     dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
#     dict2 = {'b': {'e': 4}, 'f': 5}
#     print("\nОбъединение словарей:")
#     print(deep_merge_dicts(dict1, dict2))

#     # Пример для find_most_common_values
#     test_dict = {
#         'a': 1,
#         'b': 2,
#         'c': 1,
#         'd': 3,
#         'e': 2,
#     }
#     print("\nНаиболее часто встречающиеся значения:")
#     print(find_most_common_values(test_dict))

#     # Пример для find_duplicate_values
#     test_dict_duplicates = {
#         'a': 1,
#         'b': 2,
#         'c': 1,
#         'd': 3,
#         'e': 2,
#         'f': 1,
#         'g': 4
#     }
#     print("\nДубликаты значений и их ключи:")
#     print(find_duplicate_values(test_dict_duplicates))

#     # Пример для find_dict_intersections
#     dict1 = {
#         'a': 1,
#         'b': 2,
#         'c': 3,
#         'd': 4,
#         'e':5
#     }
#     print("\nПересечения между словарями:")
#     print(find_dict_intersections(dict1, dict2))