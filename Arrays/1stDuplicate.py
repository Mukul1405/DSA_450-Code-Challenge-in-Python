
def firstDuplicate(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return arr[i]

print(firstDuplicate([1,2,2,4,3]))