class Vertex():
    def __init__(self,name, resVec):
        self.name = name
        self.resVec = resVec
        self.labelList = []
    
    def deleteVertexLabel(self,label):
        self.labelList.remove(label)
    
    # Override default equal comparison operator so we do not add two of the same
    # vertices to the list.
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.name == other.name
        return False
    
    def __str__(self):
        return (self.name)

class Edge():
    def __init__(self, outVertex, inVertex, resourceCosts, specREF):
        self.outVertex = outVertex
        self.inVertex = inVertex
        self.resourceCosts = resourceCosts
        
        # Each edge therefore has to have a specific resource extension function.
        self.specREF = specREF
    
    # Override default equal comparison operator so we do not add two of the same
    # edges to the list.
    def __eq__(self,other):
        if isinstance(other, Edge):
            return (self.outVertex == other.outVertex) and (self.inVertex == other.inVertex)
        return False
    
    def __str__(self):
        return ("{} -> {}".format(self.outVertex, self.inVertex))

class Graph():
    '''
    TODO: Cleanup edgeList, better methods for edge and node addition
    
    '''
    def __init__(self, numResources = 1, labelDomFunction = None):
        self.numberVertices = 0
        self.numberEdges = 0
        self.numberResources = numResources
        
        self.vertexList : list[Vertex] = []
        self.edgeList : list[Edge] = []
        self.edgeDict = {}
        self.labelDomination = labelDomFunction
    
    def addNode(self,name,resVec=None):
        potentialNode = Vertex(name, resVec)
        if potentialNode not in self.vertexList:
            self.vertexList.append(potentialNode)
            self.edgeDict[potentialNode.name] =[]
            self.numberVertices += 1
            return potentialNode
    
    # Notice that resource costs should be a list and specREF has to be defined on all edges.
    def addEdge(self, outVert : Vertex, inVert : Vertex, resourceCosts, specREF):
        potentialEdge = Edge(outVert, inVert,resourceCosts, specREF)
        if potentialEdge not in self.edgeList:
            self.edgeList.append(potentialEdge)
            self.edgeDict[outVert.name].append(potentialEdge)
            self.numberEdges += 1
            
    def purgeDominatedLabels(self, vertex):
        # See https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
        # Cannot remove an item from list while iterating over it in the above for loop
        vertex.labelList[:] = [label for label in vertex.labelList if not (label.isDominated and label.isProcessed)]
    
    def getAdjacencyList(self,vertex):
        return self.edgeDict[vertex.name]