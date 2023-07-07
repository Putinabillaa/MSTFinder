from Kruskal import *
from collections import defaultdict

def clustering(graph, k):
    parent = {}
    clusters = []
    
    for node in graph.nodes():
        parent[node] = node
    try:
        mst_edges, _ = kruskal(graph)
    except ValueError:
        raise ValueError
    
    for i in range(len(mst_edges) - k + 1):
        u, v = mst_edges[i]
        union(parent, u, v)
    
    for node in graph.nodes():
        clusters.append(find(parent, node))
    cluster_dict = defaultdict(list)
    
    for i, cluster in enumerate(clusters):
        cluster_dict[cluster].append(i)
    
    return list(cluster_dict.values())
