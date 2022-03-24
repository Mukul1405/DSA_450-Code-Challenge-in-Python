def rotate(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
    print(arr)

rotate([1,2,3,4])