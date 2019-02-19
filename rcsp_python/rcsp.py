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
    label_number = 1
    numberOfIterations = 0
    
    first_label = rcsp_python.defaultclasses.Label(resVert=source, resVector=[0,0])
    current_label = None
    new_label = None
    
    unprocessed_labels = queue.PriorityQueue()
    unprocessed_labels.put(first_label)
    
    while not unprocessed_labels.empty():
        current_label = unprocessed_labels.get()
        if(not current_label.isDominated):
            resident_vertex = current_label.residentVertex
            for vertexLabel in resident_vertex.labelList:
                # labelDom will return the label that IS DOMINATED.
                # This function is also defined in the Graph class
                labelDom = None
                if current_label != vertexLabel:
                    labelDom = g.labelDomination(current_label, vertexLabel)
                if (labelDom is not None):
                    labelDom.isDominated = True
            
            # See https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
            # Cannot remove an item from list while iterating over it in the above for loop
            resident_vertex.labelList[:] = [lbl for lbl in resident_vertex.labelList 
                                            if not (lbl.isDominated and lbl.isProcessed)]
        
        if(not current_label.isDominated):
            current_label.isProcessed = True
            for forwardStar in g.edgeDict[current_label.residentVertex.name]:
                new_label = forwardStar.specREF(forwardStar, current_label, label_number)
                if new_label[0]:
                    unprocessed_labels.put(new_label[1])
                    forwardStar.inVertex.labelList.append(new_label[1])
                    label_number += 1
            
        
        # Remove this label from its respective labelList because it is dominated
        else:
            current_label.residentVertex.labelList.remove(current_label)
        
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
        
        