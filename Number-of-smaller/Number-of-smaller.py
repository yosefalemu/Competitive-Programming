n,m = map(int,input().split())
ns  =  list(map(int,input().split()))
ms = list(map(int,input().split()))
 
i,j = 0,0
last_printed = 0
while i < n and j< m:
    while i < n and ns[i] < ms[j]:
        i += 1
    else:
        i -= 1
    
    print(i+1,end = " ")
    j +=1 
    i +=1
while j < m:
    print(i,end = " ")
    j+=1
