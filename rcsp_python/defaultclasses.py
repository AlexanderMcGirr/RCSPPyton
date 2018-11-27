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