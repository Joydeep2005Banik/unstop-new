from collections import deque

n=int(input())
adj=[[] for i in range(n+1)]

for j in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

dist=[-1]*(n+1)
dist[1]=0
q=deque([1])

while q:
    u=q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

print(max(dist[1:]))