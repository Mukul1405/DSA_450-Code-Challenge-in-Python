arr = [1,2,3,4,5]

def reverse(array):
    midlen = int(len(array)/2)
    print(midlen)
    for i in range(midlen):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return arr


arr = reverse(arr)
print(arr)