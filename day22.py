def insert(root,val):
    if root is None:
        return {'val':val,'left':None,'right':None}
    if val < root['val']:
        root['left']=insert(root['left'],val)
    else:
        root['right']=insert(root['right'],val)
    return root

def lvl_odr_traverse(root):
    if root is None:
        return []
    
    res=[]
    q=[root]
    front=0
    
    while front < len(q):
        lvl_size=len(q)-front
        curr_lvl=[]
        
        for i in range(lvl_size):
            node=q[front]
            front=front+1
            curr_lvl.append(str(node['val']))
            
            if node['left'] is not None:
                q.append(node['left'])
            if node['right'] is not None:
                q.append(node['right'])
        
        res.append(' '.join(curr_lvl))
    
    return res


N=int(input())
arr=list(map(int,input().split()))


root=None
for val in arr:
    root=insert(root,val)


lvls=lvl_odr_traverse(root)


for level in lvls:
    print(level)