class graph:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Methods for external use~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #Constructor
    def __init__(self,max_size,directed,weighted):
        self.max_size = max_size
        self.directed=directed
        self.weighted=weighted 
        self.graph = self.initialize_matrix()

    #Add a connection between 2 vertices
    def add(self,v1,v2,weight):
        assert v1<self.max_size,"Vertex 1 is greater than the graphs maximum size"
        assert v2<self.max_size,"Vertex 2 is greater than the graphs maximum size"
        if self.weighted:
            self.add_weighted(v1,v2,weight)    
        else:
            if weight!=None:
                print("Weight argument ignored because the graph is unweighted")
            self.add_unweighted(v1,v2)

    #prints matrix representation of graph
    def print_graph(self):
        for row in self.graph:
            line=""
            for each in row:
                line+=f"{each} "
            print(f"{line}")            

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Methods for internal use~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def initialize_matrix(self):
        matr=[]
        for i in range(self.max_size):
            matr.append([])
            for j in range(self.max_size):
                matr[i].append(0)
        return matr

    def add_unweighted(self,v1,v2):
        self.graph[v1][v2]=1
        if not self.directed:
            self.graph[v2][v1]=1

    def add_weighted(self,v1,v2,weight):
        self.graph[v1][v2]=weight
        if not self.directed:
            self.graph[v2][v1]=weight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~