
def minJumps(arr):
    if arr[0] is 0:
        return -1
    else:
        n = len(arr)
        i = 0 
        maxindex = 0
        maxvalue=0
        steps = 0
        for i in range(n):
            steps+=1
            print(i)
            for j in range(i+1,arr[i]):
                if maxvalue<j+arr[j]:
                    maxvalue=j+arr[j]
                    maxindex = j
                print(j,maxvalue)
            print()
            i = maxindex
            if maxvalue >=n:
                return steps
    return -1
arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr))


