import adjacency_matrix

#----------------------------------------------------------Searching Algos - BFS,DFS
#Recursive helper function for dfs_print
def dfs_print_helper(graph,vertex,visited):
    print(vertex)
    visited[vertex]=1
    for x in range(len(graph.graph[vertex])):
        if graph.graph[vertex][x] == 1 and visited[x]==0:
            dfs_print_helper(graph,x,visited)
    return 

#Prints out graph in dfs order using vertex 0 as root
def dfs_print(graph):
    visited =[]
    for x in range(graph.max_size):
        visited.append(0)
    dfs_print_helper(graph,0,visited)

#Recursive helper function for dfs_arr
def dfs_arr_helper(graph,vertex,visited,arr):
    arr.append(vertex)
    visited[vertex]=1
    for x in range(len(graph.graph[vertex])):
        if graph.graph[vertex][x] == 1 and visited[x]==0:
            dfs_arr_helper(graph,x,visited,arr)
    return arr

#Returns an array in bfs order using vertex 0 as root 
def dfs_arr(graph):
    visited =[]
    arr=[]
    for x in range(graph.max_size):
        visited.append(0)
    return dfs_arr_helper(graph,0,visited,arr)

#Prints out a graph in bfs order
def bfs_print(graph):
    queue = [0]
    visited =[]
    for x in range(graph.max_size):
        visited.append(0)
    print(0)
    while queue:
        vertex=queue.pop(0)
        visited[vertex]=1
        for x in range(len(graph.graph)):
            if(graph.graph[vertex][x]==1 and visited[x]==0) :
                print(x)
                visited[x]=1
                queue.append(x)
    
#Returns an array in bfs order
def bfs_arr(graph):
    output =[]
    queue = [0]
    visited =[]
    for x in range(graph.max_size):
        visited.append(0)
    output.append(0)
    while queue:
        vertex=queue.pop(0)
        visited[vertex]=1
        for x in range(len(graph.graph)):
            if(graph.graph[vertex][x]==1 and visited[x]==0) :
                output.append(x)
                visited[x]=1
                queue.append(x)
    return output

#----------------------------------------------------------Shortest path - Djikstra's 
def djikstra(graph,start):
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



#---------------------------------------------------------Demos
def test_searching_algos():
    g = adjacency_matrix.graph(max_size=7,directed=False,weighted=False)
    g.add(0,1,None)
    g.add(0,4,None)
    g.add(0,5,None)

    g.add(1,2,None)
    g.add(1,4,None)

    g.add(3,4,None)
    g.add(4,5,None)

    #g.print_graph()
    print("--------dfs_print------")
    dfs_print(g)

    print("---------dfs_arr-------")
    print(dfs_arr(g))

    print("--------bfs_print------")
    bfs_print(g)

    print("---------bfs_arr-------")
    print(bfs_arr(g))

g = adjacency_matrix.graph(max_size=7,directed=True,weighted=True)
g.add(0,1,2)
g.add(0,4,7)
g.add(0,5,8)

g.add(1,2,3)
g.add(1,4,4)

g.add(3,4,1)
g.add(4,5,2)
g.print_graph()