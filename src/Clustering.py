from Kruskal import *
import networkx as nx

def clustering(graph, k):
    ''' Return the clusters of a graph after removing k edges'''
    graph_copy = graph.copy()
    try:
        mst_edges, _ = kruskal(graph_copy)
        print(mst_edges)
    except ValueError:
        raise ValueError
    for edge in graph_copy.edges():
        if(edge not in mst_edges):
            graph_copy.remove_edge(edge[0], edge[1])
    for i in range(len(mst_edges) - 1, len(mst_edges) - k, -1):
        graph_copy.remove_edge(mst_edges[i][0], mst_edges[i][1])
    return list(nx.connected_components(graph_copy))