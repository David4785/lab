from collections import deque

def RedundantConnection(edges):
    n = len(edges)
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    q = deque(i for i in range(1, n + 1) if deg[i] == 1)
    while q:
        u = q.popleft()
        deg[u] = 0
        for v in adj[u]:
            if deg[v] > 0:
                deg[v] -= 1
                if deg[v] == 1:
                    q.append(v)

    for u, v in edges:
        if deg[u] > 0 and deg[v] > 0:
            return [u, v]


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(RedundantConnection(edges))