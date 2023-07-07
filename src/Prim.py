''' Prim's algorithm '''
def prim(graph):
    mst_edges = []
    total_weight = 0
    start_vertex = list(graph.nodes)[0]
    visited = {start_vertex}

    while len(visited) < len(graph.nodes):
        min_edge = None
        min_weight = float('inf')
        for u in visited:
            for v in graph.neighbors(u):
                if v not in visited:
                    weight = graph[u][v]['weight']
                    if weight < min_weight:
                        min_edge = (u, v)
                        min_weight = weight
        if min_edge is not None:
            u, v = min_edge
            visited.add(v)
            mst_edges.append((u, v))
            mst_edges.append((v, u))
            total_weight += min_weight
        else:
            break
    return mst_edges, total_weight
        