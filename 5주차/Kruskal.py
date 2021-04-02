parent = dict()
rank = dict()
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J'],
'edges': set([
    (3, 'A', 'B'),
    (2, 'A', 'C'),
    (4, 'A', 'D'),
    (6, 'B', 'C'),
    (5, 'B', 'E'),
    (11, 'C', 'D'),
    (5, 'C', 'E'),
    (9, 'D', 'E'),
    (7, 'B', 'F'),
    (5, 'E', 'F'),
    (7, 'E', 'G'),
    (3, 'D', 'G'),
    (1, 'F', 'G'),
    (1, 'F', 'H'),
    (2, 'H', 'G'),
    (4, 'G', 'J'),
    (3, 'H', 'J'),
    (3, 'I', 'H'),
    (6, 'I', 'F'),
    (8, 'I', 'J')])}
print(kruskal(graph))