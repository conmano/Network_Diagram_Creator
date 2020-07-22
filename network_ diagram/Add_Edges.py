"""
By: Connor Shabro

Description:
This file will be used to add edges to the Network_Diagram graph in the main document.
This is seperate from the main document so that the edges and what connects to what
is readable and easier to understand.
"""

"""
Description for add function:
This function is the original one that gets called from the main file. I have this
function here as a blocker so that it can check if the tree has any nodes and if it
does it can then call the recursive function.
"""
def add(graph, tree):
    #If there is no root node it gives the warning and returns out
    if(tree.root == None):
        print("There are no nodes present")
        return
        
    #This is the call to the recursive function
    add_rec(graph, tree.root)
    

"""
Description for add_rec function:
This function recusively calls itself to add the edges between the nodes connections.
It loops through the nodes connections left to right adding the edge and then calling the 
function on the connection node in case it has any connections.
"""
def add_rec(graph, cur):
    #This loops through all of the nodes connections
    for i in range(len(cur.connections)):
        
        #This adds the edge
        graph.add_edge(cur.name, cur.connections[i].name)
        
        #This is the recursive call of the function
        add_rec(graph, cur.connections[i])
        