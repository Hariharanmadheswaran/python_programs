def number_of_ways(n):
    arr=[0]*n 
    arr[0]=0
    arr[1]=2
    arr[2]=3 
    for i in range(3,n):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[-1]
n=int(input())
if n>1:
    print(number_of_ways(n+1)% 1000000007)
else:
    print(0)
    
