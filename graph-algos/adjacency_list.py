class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

    def has_next(self):
        if self.next ==None:
            return False
        return True

class weighted_node:
    
    def __init__(self,data,next,weight):
        self.data=data
        self.next=next
        self.weight=weight

    def has_next(self):
        if self.next == None:
            return False
        return True

class graph:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Methods for external use~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Constructor
    def __init__(self,max_size,directed,weighted):
        self.max_size=max_size
        self.directed=directed
        self.weighted=weighted
        self.graph = self.initialize_graph()

     #Add method for out of class use
    def add(self,v1,v2,weight):
        assert v1<self.max_size,"Vertex 1 is greater than the graphs maximum size"
        assert v2<self.max_size,"Vertex 2 is greater than the graphs maximum size"

        if self.weighted:
            assert weight != None ,"Weight cannot have a value of none"
            self.add_weighted(v1,v2,weight)
        else:
            if weight != None:
                print("Weight argument ignored because the graph is unweighted")
            self.add_unweighted(v1,v2)
    
    def print_graph(self):
        if self.weighted:
            for x in range(len(self.graph)):
                line_str = ""
                line_str += f"{x}: "
                currNode = self.graph[x]
                currNode=currNode.next
                while currNode != None:
                    line_str += (f"-> [Node: {currNode.data} - Weight: {currNode.weight}]")
                    currNode=currNode.next
                line_str+="\n"
                print(line_str)
        else:
            for x in range(len(self.graph)):
                line_str = ""
                line_str += f"{x}: "
                currNode = self.graph[x]
                currNode=currNode.next
                while currNode != None:
                    line_str += (f"-> [Node: {currNode.data}]")
                    currNode=currNode.next
                line_str+="\n"
                print(line_str)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Methods for internal use~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Method to initialize the array of linked lists
    def initialize_graph(self):
        arr=[]
        if self.weighted:
            for x in range(self.max_size):
                arr.append(weighted_node(None,None,None))
        else:
            for x in range(self.max_size):
                arr.append(node(None,None))
        return arr 

    #Connects 2 vertices with an unweighted edge
    def connect_vertices_unweighted(self,v1,v2):
        currNode = self.graph[v1]
        while(currNode.has_next()):
            currNode=currNode.next
        currNode.next=node(v2,None)

    #Connects 2 vertices with a weighted edge
    def connect_vertices_weighted(self,v1,v2,weight):
        currNode = self.graph[v1]
        while(currNode.has_next()):
            currNode=currNode.next
        currNode.next=weighted_node(v2,weight,None)
    
    #Adds edge between 2 vertices with an unweighted edge
    def add_unweighted(self,v1,v2):
        #Connect v1 -> v2
        self.connect_vertices_unweighted(v1,v2)
        #Connects v2 -> v1 if graph is not directed
        if not self.directed:
            self.connect_vertices_unweighted(v2,v1)

    #Adds edge between 2 vertices with a weighted edge
    def add_weighted(self,v1,v2,weight):
        #Connect v1 -> v2
        self.connect_vertices_weighted(v1,v2,weight)
        #Connects v2 -> v1 if graph is not directed
        if not self.directed:
            self.connect_vertices_weighted(v2,v1,weight)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~