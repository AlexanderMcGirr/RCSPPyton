class Vertex():
    def __init__(self,name, resVec):
        self.name = name
        self.resVec = resVec
        self.labelList = []
    
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

class Label():
    ''' 
    According to Boost documentation labels in SPPRC stores:
        
        -Resident vertex
        -Predecessor Arc over which it has been extended
        -Predecessor label
        -Current Vector of resource values    
    '''
    def __init__(self, resVert=None,predEdge=None,predLabel=None,
                  resVector=None, labelID=0):
        self.residentVertex = resVert
        self.predEdge = predEdge
        self.predLabel = predLabel
        self.resourceVector = resVector
        
        self.isDominated = False
        self.isProcessed = False
        self.isFeasible = True
        self.id = labelID
    
    def __eq__(self,other):
        if isinstance(other, Label):
            return ((self.resourceVector == other.resourceVector) 
                    and (self.id == other.id))
    
    def __ne__(self,other):
        if isinstance(other, Label):
            for first,second in zip(self.resourceVector, other.resourceVector):
                if second != first:
                    return True
            return (self.id != other.id)
    
    def __lt__(self, other):
        if isinstance(other, Label):
            for first,second in zip(self.resourceVector, other.resourceVector):
                if second <= first:
                    return False
            return True
    
    def __le__(self,other):
        if isinstance(other, Label):
            for first,second in zip(self.resourceVector, other.resourceVector):
                if second < first :
                    return False
            return True
        
    def __gt__(self, other):
        if isinstance(other, Label):
            for first,second in zip(self.resourceVector, other.resourceVector):
                if second >= first :
                    return False
            return True    
    
    def __ge__(self,other):
        if isinstance(other, Label):
            for first,second in zip(self.resourceVector, other.resourceVector):
                if second > first :
                    return False
            return True

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