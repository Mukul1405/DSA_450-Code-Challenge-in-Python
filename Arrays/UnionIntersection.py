def unionIntersection(arr1,arr2):
    unionarr = []
    intersect = []
    for i in arr1:
        if i in arr2:
            intersect.append(i)
    
    for i in arr1:
        if i not in unionarr:
            unionarr.append(i)
    for i in arr2:
        if i not in unionarr:
            unionarr.append(i)

    print(unionarr,intersect)

unionIntersection([1,2,4,5],[2,3,5,6,7,8])