import sys
sys.setrecursionlimit(10**6)

def solve():
    n, m = map(int, sys.stdin.readline().strip().split())
    
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u-1].append(v-1)  
    
    
    visited = [False] * n
    order = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        order.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    reverse_graph = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            reverse_graph[v].append(u)
    
    visited = [False] * n
    scc_id = [-1] * n
    scc_count = 0
    
    def dfs2(node, scc_id_val):
        visited[node] = True
        scc_id[node] = scc_id_val
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, scc_id_val)
    
    for node in reversed(order):
        if not visited[node]:
            dfs2(node, scc_count)
            scc_count += 1
    
    in_degree = [0] * scc_count
    
    for u in range(n):
        for v in graph[u]:
            if scc_id[u] != scc_id[v]:

                in_degree[scc_id[v]] += 1
    
    result = sum(1 for i in range(scc_count) if in_degree[i] == 0)
    
    print(result)

if __name__ == "__main__":
    solve()