"""
question :
Sherlock thinks he is always good at counting .
so ,he decided to count the total number of squares in n*n grid given to him,
but,he struggles in doing so and needs your help now.

eg :
input  2
output 5  (total number of squares in 2*2 grid)
"""
# solution
inp=int(input("ENTER THE VALUE OF N FOR N*N GRID "))
arr=[]
for i in range(inp):
    arr.append([1]*inp)
result=0
for i in range(inp*inp):
    var=i//inp
    j=i%inp
    while True:
        try:
            if arr[var][j]:
                result+=1
#                 print(var,j)
        except:
            break
        var+=1
        j+=1
print(f"THE NUMBER OF SQAURES IN {inp}*{inp} GRID IS {result}")
