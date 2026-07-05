class Node:
    def __init__(self, node_id, value, next_id):
        self.node_id = node_id
        self.value = value
        self.next_id = next_id
        self.next = None

def recover_chain(n, node_details, start_id):
    # User logic goes here
    nodes={}
    for node_id,value,next_id in node_details:
        nodes[node_id]=Node(node_id,value,next_id)
    
    for node in nodes.values():
        if node.next_id != -1 and node.next_id in nodes:
            node.next=nodes[node.next_id]
    
    start=nodes.get(start_id)
    if not start:
        return []
    
    slow=start
    fast=start
    cycle=False
    
    while fast and fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            cycle=True
            break
    
    if cycle:
        slow=start
        while slow != fast:
            slow=slow.next
            fast=fast.next
        
        cycle_start = slow
        prev=cycle_start
        curr=cycle_start.next
        while curr != cycle_start:
            prev=curr
            curr=curr.next

        prev.next=None
        prev.next_id=-1
    
    result=[]
    curr=start
    while curr:
        result.append(curr.value)
        curr=curr.next
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    n = int(data[0])
    node_details = []
    for i in range(1, n + 1):
        node_id, value, next_id = map(int, data[i].split())
        node_details.append((node_id, value, next_id))
    start_id = int(data[n + 1])
    result = recover_chain(n, node_details, start_id)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()