n,k=map(int,input().strip().split())
p=list(map(int,input().strip().split()))

def heap(arr):
    m=len(arr)
    for i in range(m // 2 -1,-1,-1):
        downshift(arr,i,m)

def downshift(arr,idx,size):
    largest=idx
    left=2*idx+1
    right=2*idx+2

    if left < size and arr[left] > arr[largest]:
        largest=left
    if right < size and arr[right] > arr[largest]:
        largest=right

    if largest != idx:
        arr[idx],arr[largest]=arr[largest],arr[idx]
        downshift(arr,largest,size)

def max(arr,s):
    arr[0],arr[s-1]=arr[s-1],arr[0]
    s=s-1
    downshift(arr,0,s)
    return arr[s],s

heap(p)
heap_s=n

res=[]
for i in range(k):
    max_val,heap_s=max(p,heap_s)
    res.append(max_val)

print(' '.join(map(str,res)))