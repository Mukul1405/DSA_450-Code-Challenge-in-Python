arr = [1,3,-5,-11,4,10]

def kthmin(k,array):
    array.sort()
    return array[k-1]

print(kthmin(3,arr))