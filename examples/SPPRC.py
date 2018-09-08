if __name__ == '__main__':
    import rcsp_python
    
    def labelDomination(firstLabel, secondLabel):
        if firstLabel.resourceVector[0] <= secondLabel.resourceVector[0]:
            return secondLabel
        elif secondLabel.resourceVector[0] <= firstLabel.resourceVector[0]:
            return firstLabel
        else:
            return None
    
    def specREF(edge, label, labelNum):
        newCost = label.resourceVector[0] + edge.resourceCosts[0]
        newTime = label.resourceVector[1] + edge.resourceCosts[1] 
        
        newResVec = [newCost, newTime]        
        feasible = True
        
        return (feasible, rcsp_python.Label(edge.inVertex, 
                                         edge, label, newResVec, labelNum))
    
    
    G = rcsp_python.Graph(2, labelDomination)     
    
    # Add nodes
    A = G.addNode("A")
    B = G.addNode("B")
    C = G.addNode("C")
    D = G.addNode("D")
    E = G.addNode("E")
    
    # Add edges with resource costs, and the resource extension Function
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