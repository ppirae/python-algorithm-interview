# 수도코드
DFS-iterative(G, v)
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do
                S.push(w)


# 파이썬 코드
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v is not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.push(w)
    return discovered
