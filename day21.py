n=int(input().strip())
cost=[]


for i in range(n+1):
    cost.append(list(map(int, input().strip().split())))


inf=10**18
dp=[]   
       
for i in range(1 << n): 
    dp.append([inf]*(n+1)) 

for i in range(1,n+1):
    dp[1 << (i-1)][i]=cost[0][i]


for k in range(1 << n):
    for i in range(1,n+1):
        if dp[k][i] == inf:
            continue
        for j in range(1,n+1):
            if k & (1 << (j-1)):
                continue
            new_k=k | (1 << (j-1))
            dp[new_k][j]=min(dp[new_k][j],dp[k][i]+cost[i][j])


full_k=(1 << n)-1
ans=inf
for i in range(1,n+1):
    ans=min(ans,dp[full_k][i]+cost[i][0])

print(ans)