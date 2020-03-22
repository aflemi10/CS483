import adjacency_list

#----------------------------------------------------------Searching Algos - BFS,DFS
def bfs_print(graph):
    return None

def bfs_arr(graph):
    return None

def dfs_print(graph):
    return None

def dfs_arr(graph):
    return None
#----------------------------------------------------------Shortest path - Djikstra's 
def djikstra(graph):
    assert graph.weighted,"Graph supplied as an argument is not weighted"

#----------------------------------------------------------Minimum Spanning Tree - Prim's, Kruskal
def prim(graph):
    return None

def kruskal(graph):
    return None

#----------------------------------------------------------Additional
def cycle_detection(graph):
    return None

def tree_detection(graph):
    return None

def testing_biparteness(graph):
    return None 

g = adjacency_list.graph(max_size=7,directed=False,weighted=False)
g.add(0,1,None)
g.add(0,2,None)

g.add(1,3,None)
g.add(1,4,None)

g.add(2,5,None)
g.add(2,6,None)

g.print_graph()