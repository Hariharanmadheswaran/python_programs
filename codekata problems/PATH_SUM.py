"""
PATH_SUM --QUESTION TAKEN FROM LEETCODE

QUESTION:

    GIVEN THE ROOT OF BINARY TREE AND INTEGER TARGETSUM ,RETURN TRUE IF TREE HAS ROOT-TO-LEAF PATH SUCH THAT ADDING UP
    ALL TOGETHER ALONG PATHS EQUALS TARGETSUM.

    A LEAF NODE IS A NODE WITH NO CHILD
"""



def path_sum(target,index,current):
    if current ==target:
        if (2*index)+1>=len(arr) and (2*index)+2>=len(arr): # checking last index is a leaf node leaf node
            return True
        return False
    if (2*index)+1<len(arr):
        if current+arr[2*index+1]<=target:
            return path_sum(target,(2*index)+1,current+arr[2*index+1])
    if (2*index)+2<len(arr):
        if current + arr[2 * index + 2] <= target:
            return path_sum(target, (2 * index )+ 2, current + arr[(2*index)+2])
    return False

arr=[5,4,8,11,0,13,4,7,2,0,0,0,1]
target=22

if arr!=[]:
    print(path_sum(target,index=0,current=arr[0]))
else:
    print(False)