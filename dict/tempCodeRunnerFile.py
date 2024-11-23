{0: 10, 1: 20}
def continue_dict(obj):
    max_key = max(obj.keys())
    obj[max_key + 1] = (max_key * 10) + 10
    return obj
print(continue_dict(x))