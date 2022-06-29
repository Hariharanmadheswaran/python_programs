"""
question :  MERGE TWO GIVEN SORTED ARRAYS

INPUT  : A1=[1,2,3,4,5]
         A2=[2,4,5,5]

OUTPUT :  [1,2,2,3,4,4,4,5,5]
"""
arr1=list(map(int,input("enter your first sorted array :").split()))

arr2=list(map(int,input("enter your second sorted array :").split()))

i,j=0,0
merged_array=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        merged_array.append(arr1[i])
        i+=1
    else:
        merged_array.append(arr2[j])
        j += 1
while i<len(arr1):
        merged_array.append(arr1[i])
        i += 1
while j<len(arr2):
        merged_array.append(arr2[j])
        j += 1
print("THE SORTED  ARRAY AFTER MERGING IS ",merged_array)