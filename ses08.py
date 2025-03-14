# This command imports data structures from ses08_graphs.py
# It will only work if the ses08_graphs.py file is in the same directory
import ses08_graphs as gs


def lecture_graph():
    """
    Returns the lecture directed graph example adjacency list as a dictionary
    
    Complete the dictionary below
    
    Examples:
    >>> adj_list = lecture_graph()
    >>> adj_list['d']['e']
    2
    >>> 'd' in adj_list['e']
    False
    >>> [adj_list[n][m] for n in 'abcde' for m in 'abcde' if m in adj_list[n]]
    [1, 5, 2, 5, 2, 6, 2]
    >>> [len(adj_list[n]) for n in 'abcde']
    [2, 2, 2, 1, 0]
    """
    distances = {
        'a': {'b': 1, 'd': 5},
        'b': {'c': 2, 'd': 5},
        'c': {'a': 2, 'e': 6},
        'd': {'e': 2},
        'e': {}
    }
    
    return distances


def dijkstra(graph, start):
    """ 
    Shortest distances using Dijkstra's algorithm 
    
    Polynomial-time implementation. 
    (Should use a set, but prefers an ordered list for the doctests)
    
    Assumes that there is a path from start node to all other nodes in graph.
    
    Parameters:
        graph: a Graph (or Digraph) 
        start: starting node for the algorithm
    Returns: 
        dists: dictionary containing shortest distances to all nodes
        prev_nodes: dictionary containing the previous node from which each node was explored
                None for the starting node
    
    Examples:
    >>> graph = gs.Digraph(lecture_graph())
    >>> dists, prev_nodes = dijkstra(graph, 'a')
    >>> [dists['b'], dists['e'], dists['c'], dists['d']]
    [1, 7, 3, 5]
    >>> [prev_nodes['a'], prev_nodes['e'], prev_nodes['c'], prev_nodes['d']]
    [None, 'c', 'b', 'a']
    """
    
    
    X = [start]
    
    prev_nodes = {start: None}  
    
    A = dict() 
    for node in graph.get_nodes(): 
        A[node] = float('Inf')  
        
    A[start] = 0  

   
    while len(X) < len(graph.get_nodes()): 
         
        min_edge = []  # List [src, dest, weight]
        min_dist = float('inf')
        
        
        for src in X:
            for dest, weight in graph.children_of(src): 
                
                    if A[src] + weight < min_dist: 
                        min_edge = [src, dest, weight] 
                        min_dist = A[src] + weight 
              
        A[min_edge[1]] = A[min_edge[0]] + min_edge[2]
        
        X.append(min_edge[1])  
        
        prev_nodes[min_edge[1]] = min_edge[0]
    
    return A, prev_nodes

def print_path(prev_nodes, v):
    """ 
    Based on dictionary prev_nodes containing links to previous nodes, 
    prints out path from starting node to v.
    """
    path_list = []
    while v is not None:
        path_list.append(v)
        v = prev_nodes[v]
    
    path_list = reversed(path_list)    
    path = ' -> '.join(path_list)
    print(path)

