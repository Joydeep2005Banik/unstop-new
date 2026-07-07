n=int(input())
crystal=list(map(int,input().split()))

if n == 0:
    print(0)
elif n == 1:
    print(crystal[0])
else:
    dp=[0]*n
    dp[0]=crystal[0]
    dp[1]=max(crystal[0],crystal[1])
    
    for i in range(2, n):
        dp[i]=max(dp[i-1],crystal[i]+dp[i-2])
    
    print(dp[-1])