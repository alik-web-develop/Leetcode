# # ////////////task1
# # x = {
# #     "two": 2,
# #     "fist": 1,
# #     "three": 3
# # }


# #             if arr[i][1] > arr[i + 1][1]:
# #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# #     return arr
# # print(sort_of_value65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# # def filtration_for_physique(students,height,weight):
# #     result = {}
# #     for key,val in students.items():
# #         if val[0] >= height and 
# # print(str_to_int_in_dict(x))

# #     result = []
# #     {result.append(i) 
# # ............task57s():
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