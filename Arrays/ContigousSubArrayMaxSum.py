

def maxsum(arr):
    max = arr[0]
    sum = 0 
    for i in arr:
        sum+=i
        if max < sum:
            max = sum
        if sum < 0:
            sum =0
    return max


print(maxsum([1,-2,3,-4,9]))