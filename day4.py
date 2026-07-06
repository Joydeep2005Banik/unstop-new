t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    if len(set(arr)) < n:
        print("YES")
    else:
        print("NO")