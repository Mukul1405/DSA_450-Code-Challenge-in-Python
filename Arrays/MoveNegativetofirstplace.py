

def moveNeg(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]<0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j+=1
    print(arr)

moveNeg([-12, 11, -13, -5, 6, -7, 5, -3, -6])