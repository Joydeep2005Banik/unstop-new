n=int(input())
l=[]

for i in range(n):
    x=input().split()
    if x[0] == "ADD":
        l.append(int(x[1]))
    else:
        if l:
            l.pop()

if l:
    print(l[-1])
else:
    print(-1)