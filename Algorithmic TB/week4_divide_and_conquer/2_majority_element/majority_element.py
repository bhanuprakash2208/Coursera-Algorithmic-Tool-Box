n=int(input())
l=list(map(int,input().split()))
d={}
m=n//2
for i in l:
    d[i]=d.get(i,0)+1
flag=0
for value in d.values():
    if value>m:
        flag=1
        print(1)
        break
if flag==0:
    print(0)
    
       
