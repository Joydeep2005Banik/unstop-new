# Read the dimensions
r,c=map(int,input().strip().split())

grid=[]


for i in range(r):
    row=list(map(int,input().strip().split()))
    grid.append(row)


for i in range(r):
    grid[i]=grid[i][::-1]

for row in grid:
    print(' '.join(map(str,row)))