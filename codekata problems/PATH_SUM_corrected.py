"""
PATH_SUM --QUESTION TAKEN FROM LEETCODE
i just made some corrected which i found later wrong 
"""



def path_sum(target,index,current):
    if current>target or arr[index]==0:
        return ""

    var = index
    if arr[:index].count(0) > 0:
        var = index - 1

    if current ==target:
        if ((2*var)+1>=len(arr) and (2*var)+2>=len(arr)) or (arr[2*var+1]==0 and arr[2*var+2]==0): # checking last index is a leaf node leaf node
            return "True"
        return ""

    if (2*var)+2<len(arr):
        return path_sum(target,(2*var)+1,current+arr[2*var+1])+path_sum(target, (2 * var )+ 2, current + arr[(2*var)+2])
    elif (2*var)+1<len(arr):
                return path_sum(target, (2 * var )+ 1, current + arr[(2*var)+1])
    return ""

arr=[5,4,8,11,0,13,4,7,2,0,0,0,1]
target=27

if arr!=[]:
    print(False if path_sum(target,index=0,current=arr[0])=="" else True )
else:
    print(False)