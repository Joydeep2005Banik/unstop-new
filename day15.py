n=int(input().strip())
p=list(map(int,input().strip().split()))

dp=[[0]*n for j in range(n)]

for l in range(2,n+1):
    for i in range(n-l+1):
        j=i+l-1
        dp[i][j]=float('inf')
        
        for k in range(i,j):
            cost=dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1]
            
            if cost < dp[i][j]:
                dp[i][j]=cost

print(dp[0][n-1])