n,d=map(int,input().split())
distance=list(map(int,input().split()))

distance.sort()

count=1
last_position=distance[0]

for i in range(1,n):
    if distance[i]-last_position >= d:
        count=count+1
        last_position=distance[i]

print(count)