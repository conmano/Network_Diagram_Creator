"""
By: Connor Shabro

Description:
This file will be used to create a directed graph
The directed graph will represent the network connections in reference to the CDE


Modules:
-networkx: This will be used to input the nodes and edges. It can also hold
attributes so that the nodes contain more data.

-matplotlib.pyplot: This will be used to show and save the graph created. 

-csv: This is used to take in the comma dilimetered csv data


Supporting files:
Add_Nodes.py
Add_Edges.py
Add_Images.py
Network_Tree.py

""" 

#Import declarations
import networkx as nx
import matplotlib.pyplot as plt
import Add_Nodes
import Add_Edges
import Add_Images
import Network_Tree
import csv

#Creates the diagram
Network_Diagram = nx.DiGraph()


#This opens and gets information from csv file
with open(r"C:\Users\Connor\Desktop\network_ diagram\Network_Diagram.csv") as f:
    reader = csv.reader(f)
    next(reader)
    network = []
    for row in reader:
        network.append(row)

#This uses the Network_Tree file to create the tree of nodes
tree = Network_Tree.Tree(network)

#This prints off the tree so that you can make sure each node is in it
tree.print_tree()

#This calls the method to add all the nodes to the graph
Add_Nodes.add(Network_Diagram, tree)

#This calls the method to add all the edges to the graph
Add_Edges.add(Network_Diagram, tree)

#This is the code to set up variables that will be used to locate the
#positions of the nodes in the diagram. It then hands this information off 
#to the Add_Images file
pos = nx.spring_layout(Network_Diagram)
plt.figure(figsize = (15,9))
ax = plt.gca()
fig = plt.gcf()
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.02

#This draws the diagram before images are inserted which will be shown with pyplot
nx.draw_networkx(Network_Diagram, pos, width = 1, with_label = True, node_color = 'white', font_size = 8, node_size = 500)
 
#This is the call to the Add_Images file that inserts the images on their respective nodes
Add_Images.add(Network_Diagram, tree, pos, trans, trans2, imsize)

#This displays the finished diagram
plt.show()