''' Kruskal algorithm '''
def kruskal(graph):
    mst_edges = []
    total_weight = 0
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    parent = {v: v for v in graph.nodes}
    for u, v, attrs in edges:
        if find(parent, u) != find(parent, v):
            mst_edges.append((u, v))
            union(parent, u, v)
            total_weight += attrs['weight']
    return mst_edges, total_weight

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    parent[root_v] = root_u