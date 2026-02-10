# # ////////////task1
# # x = {
# #     "two": 2,
# #     "fist": 1,
# #     "three": 3
# # }


# #             if arr[i][1] > arr[i + 1][1]:
# #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
# #     return arr
#h)
#     return result

# # Задача: Объединить словари с учетом вложенности
# def deep_merge_dicts(
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
#     common_keys = list(s
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