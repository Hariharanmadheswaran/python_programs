"""
QUESTION --MEDIUM LEVEL (LEETCODE)
    GIVEN A COLLECTION OF NUMBERS,NUMS THAT MIGHT CONTAIN DUPLICATES RETURN ALL POSSIBLE
    UNIQUE PERMUTATION IN ANY ORDER.
    INPUT:
        NUMS=[1,1,2]
    OUTPUT:
        [[1,1,2],[1,2,1],[2,1,1]]
"""

def backtrack(inter,n):
    if len(inter)==n:
        res.append(inter.copy())
        return
    dup=[]
    for i in range(len(arr)):
        if arr[0] in dup:
            val=arr.pop(0)
            arr.append(val)
            continue
        val=arr.pop(0)
        dup.append(val)
        inter.append(val)
        backtrack(inter,n)
        inter.pop()
        arr.append(val)

if __name__=="__main__":
    res=[]
    sets= set()
    arr=[1,2,1]
    backtrack([],len(arr))
    print(res)

