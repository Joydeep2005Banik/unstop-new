def insert(root,val):
    if root is None:
        return [val,None,None] 
    if val < root[0]:
        root[1]=insert(root[1],val)
    else:
        root[2]=insert(root[2],val)
    return root

def postorder(root,result):
    if root is None:
        return
    postorder(root[1],result)
    postorder(root[2],result)
    result.append(root[0])

def main():
    N=int(input().strip())
    arr=list(map(int,input().strip().split()))
    
    root=None
    for num in arr:
        root=insert(root,num)
    
    result=[]
    postorder(root,result)
    print(' '.join(map(str,result)))

if __name__ == "__main__":
    main()