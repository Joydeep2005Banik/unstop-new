n=int(input().strip())
e=list(map(int,input().strip().split()))

dp=[float('inf')]*n
dp[0]=0

for i in range(1,n):
    for j in range(i):
        cost=dp[j]+abs(e[j]-e[i])*(i-j)
        if cost < dp[i]:
            dp[i]=cost

print(dp[n-1])