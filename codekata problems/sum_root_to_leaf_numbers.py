"""
        THE QUESTION IS TAKEN FROM LEETCODE
"""

def sum_root_to_leaf(arr,index,elements):
    if (2*index)+1>=len(arr) and (2*index)+2>=len(arr):
        elements=[str(i) for i in elements]
        return ["".join(elements)]

    path=[]
    if (2*index)+1<len(arr):
        for i in sum_root_to_leaf(arr,(2*index)+1,elements+[arr[(2*index)+1]]):
            path.append(i)
    if (2*index)+2<len(arr):
        for i in sum_root_to_leaf(arr,(2*index)+2,elements+[arr[(2*index)+2]]):
            path.append(i)
    return path

if __name__=="__main__":
    # arr=list(map(int,input("ENTER THE NUMBERS (SPACE SEPERATED)").split()))
    arr=[4,9,0,5,1]
    index=0
    elements=[arr[0]]
    result=[int(i) for i in sum_root_to_leaf(arr,index,elements)]
    print("THE POSSIBLE WAYS :",result)
    print("SUM ROOT TO LEAF (THE SUMMATION OF NUMBERS)",sum(result))


