arr = [1,2,6,-5,5]

def minmax(array):
    min = array[0]
    max = array[0]
    for i in range(1,len(array)):
        if array[i]<min:
            min = array[i]
        if array[i]>max:
            max = array[i]
    return (min,max)

print(minmax(arr))

