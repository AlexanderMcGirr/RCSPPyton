# Testing if the algorithm works based on Boost example:
# https://www.boost.org/doc/libs/1_68_0/libs/graph/example/r_c_shortest_paths_example.cpp

# Resource constrained shortest path problem with Time Windows example
if __name__ == '__main__':
    import rcsp_python
    import collections
    
    # Domination function
    def labelDomination(firstLabel :rcsp_python.Label, secondLabel :rcsp_python.Label):
        '''
        Parameters: firstLabel -> First label (should be current_label)
                    secondLabel -> Second label should be in resident vertex list
        
        Return : Label that IS DOMINATED or None if no domination    
        '''
        # This function should return the label that IS dominated
        labelOneLessThanEqual = False
        labelTwoLessThanEqual = False
        for first, second in zip(firstLabel.resourceVector, secondLabel.resourceVector):
            if first < second:
                labelOneLessThanEqual = True
            if second < first:
                labelTwoLessThanEqual = True
            
            # If one label does not dominate then we can stop comparisons
            if labelOneLessThanEqual and labelTwoLessThanEqual:
                break
        
        # If both labelOneLessThanEqual and labelTwoLessThanEqual are None then
        # they are equal over all values in resourceVector, then the tie-breaker is to
        # return the first label
        if (labelOneLessThanEqual == False) and (labelTwoLessThanEqual == False):
            return firstLabel
        
        # If they are both true then one does not dominate the other so return None
        if labelOneLessThanEqual and labelTwoLessThanEqual:
            return None
        
        # labelOne is strictly less than labelTwo in at least one element
        # labelTwo is then dominated
        if labelOneLessThanEqual and (labelTwoLessThanEqual == False):
            return secondLabel
        
        # labelTwo is strictly less than labelOne in at least one element
        # labelOne is then dominated
        if (labelOneLessThanEqual == False) and labelTwoLessThanEqual:
            return firstLabel
    
    
    G = rcsp_python.Graph(2, labelDomination)
     
    # Add nodes with Time Windows as resources.
    A = G.addNode("A", [0,0])
    B = G.addNode("B", [5,20])
    C = G.addNode("C", [6,10])
    D = G.addNode("D", [3,12])
    E = G.addNode("E", [0,100])
     
    # Resource extension function
    def specREF(edge,label, labelNum):
        # Take the edge costs and add them    
        newCost = label.resourceVector[0] + edge.resourceCosts[0]
        newTime = label.resourceVector[1] + edge.resourceCosts[1]
    
        
        if newTime < edge.inVertex.resVec[0]:
            newTime = edge.inVertex.resVec[0]    
        
        newResVec = [newCost,newTime]    
        
        # Now return a tuple with bool if feasible and new label
        feasible = False
        if newTime <= edge.inVertex.resVec[1]:
            feasible = True
        
        NamedLabel = collections.namedtuple('NewLabel', 'feasibility label')
        
        return NamedLabel( feasible, rcsp_python.Label(edge.inVertex, edge, label, newResVec, labelNum) )
    
    
    # Add edges with the cost and time cost of each edge
    
    G.addEdge(A, C, [1,5], specREF)
    G.addEdge(B, B, [2,5], specREF)
    G.addEdge(B, D, [1,2], specREF)
    G.addEdge(B, E, [2,7], specREF)
    G.addEdge(C, B, [7,3], specREF)
    G.addEdge(C, D, [3,8], specREF)
    G.addEdge(D, E, [1,3], specREF)
    G.addEdge(E, A, [1,5], specREF)
    G.addEdge(E, B, [1,4], specREF)
    
    solutions = rcsp_python.rcsp(G, A , E)
    rcsp_python.printRCSP(solutions)

# Output:
# Path:ACBDE
# Accumulated Costs: [10, 14]