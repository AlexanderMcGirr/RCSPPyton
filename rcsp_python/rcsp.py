import rcsp_python.defaultclasses
import queue

# Algorithm is based off Boost RCSP
# https://www.boost.org/doc/libs/1_68_0/libs/graph/doc/r_c_shortest_paths.html
def rcsp(g, source, terminal):
    '''    
    Parameters: g -> Graph
                source -> Vertex
                terminal -> Vertex
    
    Returns: List of labels at terminal vertex.
    
    Resource extension functions should be an attribute of the arc 
    Label domination function should be an attribute of the graph
    
    Resource extension function should be of the following prototype:
        
        REF(edge, label, labelNum) -> (bool,new Label)
        
    Where bool denotes the feasibility of the label and new label is the label,
    both within a tuple.
    
    The label domination function should be of the following prototype:
        
        labelDomination(firstLabel, secondLabel) -> Label/None
        
    This function should return the label that is dominated or None,
    if there is no domination.
    
    Both these functions are defined by the user, so it can be very flexible.
    '''
    labelNumber = 1
    numberOfIterations = 0
    
    firstLabel = rcsp_python.defaultclasses.Label(resVert=source, resVector=[0,0])
    currentLabel = None
    newLabel = None
    
    unprocessedLabels = queue.PriorityQueue()
    unprocessedLabels.put(firstLabel)
    
    while not unprocessedLabels.empty():
        currentLabel = unprocessedLabels.get()
        labelVertex = currentLabel.residentVertex
        if(not currentLabel.isDominated):            
            for vertexLabel in labelVertex.labelList:
                # labelDom will return the label that IS DOMINATED.
                # This function is also defined in the Graph class
                labelDom = None
                if currentLabel != vertexLabel:
                    labelDom = g.labelDomination(currentLabel, vertexLabel)
                if (labelDom is not None):
                    labelDom.isDominated = True
            
            
            g.purgeDominatedLabels(labelVertex)
        
        if(not currentLabel.isDominated):
            currentLabel.isProcessed = True
            for forwardStar in g.getAdjacencyList(labelVertex):
                # newLabel should return a named tuple with fields: feasibility, label
                newLabel = forwardStar.specREF(forwardStar, currentLabel, labelNumber)
                if newLabel.feasibility:
                    unprocessedLabels.put(newLabel.label)
                    forwardStar.inVertex.labelList.append(newLabel.label)
                    labelNumber += 1
            
        
        # Remove this label from its respective labelList because it is dominated
        else:
            currentLabel.residentVertex.labelList.remove(currentLabel)
        
        numberOfIterations +=1
     
    #print("Number of Iterations: {}".format(numberOfIterations))
    return terminal.labelList

def printRCSP(labelList):
    paretoSolutions = []
    for solution in labelList:
        # Create a new list for each solution
        tempList = []
        labelIterator = solution
        # Take the first terminal label and append to list
        while labelIterator:
            tempList.append(labelIterator)
            labelIterator = labelIterator.predLabel
        paretoSolutions.append(tempList)
    
    # For each solution print in reverse order
    for solution in paretoSolutions:
        accumulatedResourceVector = solution[0].resourceVector
        print("Path:",end='')
        for s in reversed(solution):
            print("{}".format(s.residentVertex), end='')
        print()
        print("Accumulated Costs: {}".format(accumulatedResourceVector))
        
        