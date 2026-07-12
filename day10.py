n=int(input())
vid=list(map(int,input().split()))

f={}

for i in vid:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1

max=-1
active=None

for i,c in f.items():
    if c > max or (c == max and i < active):
        max=c
        active=i

print(active, max)