
def sort012(arr):
    count0,count1,count2=0,0,0
    for i in arr:
        if i is 0:
            count0+=1
        elif i is 1:
            count1+=1
        else:
            count2+=1
    
    for i in range(0,count0):
        arr[i] = 0
    for i in range(count0,count0+count1):
        arr[i] = 1
    for i in range(count0+count1,count0+count1+count2):
        arr[i] = 2

    print(arr)


array = [0,1,2,0,1,2,0,1,2,1]
sort012(array)