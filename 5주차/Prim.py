def setAdj(G):
    Adj = dict()
    for v in G['vertices']:
        Adj[v] = []
    for e in G['edges']:
        weight,u,v = e
        Adj[u].append(e)
    return Adj
def PrimMST(G, Adj):
    T = dict()
    Bound = []
    p = G['vertices'][0]
    T[p] = "start"
    while len(T) < len(G['vertices']):
        for e in Adj[p]:
        w, p, u = e
        if u in T:
            Bound.remove((w, u, p))
        else:
            Bound.append(e)
        mine = min(Bound, key=lambda x:x[0])
        p = mine[2]
        T[p] = mine
    return T 
graph = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],'edges': [(7, 'A', 'B'),(11, 'G', 'F')]}
Adj = setAdj(graph)
print(PrimMST(graph, Adj))
