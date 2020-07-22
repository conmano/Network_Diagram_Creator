"""
By: Connor Shabro

Description:
This file will handle the function of adding nodes to the Network_Diagram.
This is a seperate file so that the managment of nodes is not jumbled in the
main document.
"""

"""
Description for add function:
The add function is simple in that it runs through the linear list of nodes
and adds them into the graph node storage.
"""
def add(graph, tree):
    #This loops through the tree node and inserts their name and IP into the networkx node storage
    for i in range(len(tree.nodes)):
            graph.add_node(tree.nodes[i].name, ip = tree.nodes[i].IP)
        