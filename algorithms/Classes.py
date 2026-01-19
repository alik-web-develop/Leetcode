# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

def locate(arr,locator):
    counter = 0
    while counter < len(arr):
        for i in range(counter, len(arr)):
            if arr[counter] + arr[i] == locator:
                return [counter, i]
            print(arr[counter], arr[i])
        counter += 1
    return "dolbaeb"
nums = [7,11,15,2,65,123,0,90,11]
target = 22
print(locate(nums,target))