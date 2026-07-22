n=int(input())
q=[]
for i in range(n):
    x=input().split()

    if x[0] == "ENTER":
        q.append(x[1])
    else:
        if q:
            q.pop(0)

if q:
    print(q[0])
else:
    print("EMPTY")