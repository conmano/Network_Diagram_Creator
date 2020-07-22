"""
By Connor Shabro

Description:
This will add images to the individual nodes. I will add the images based on the computer type value. 
The computer type value will be a number.


Modules:
-maptplotlib.image: This is used to save the read in image in a variable so 
that it can be placed on the plot based on specific location settings you give it.

-matplotlib.pyplot: This is used to get the axis of the graph which are used
to properly place the image on top of the node.


dType: 0 = Other, 1 = Firewall, 2 = Interface, 3 = Terminal, 4 = Switch
"""

#Import declarations
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

"""
Description of add function:
The add function starts off by placing the image files into their labeled varaibles 
so that instead of reading the image in at each loop it only has to do it once per 
function call. Afterwards it loops through the nodes placing their respective images.
"""
def add(graph, tree, pos, trans, trans2, imsize):
    
    #This is the declaration of the image variables
    firewallImg = mpimg.imread(r"C:\Users\Connor\Desktop\network_ diagram\Firewall.png")
    interfaceImg = mpimg.imread(r"C:\Users\Connor\Desktop\network_ diagram\Interface_Fake.png")
    switchImg = mpimg.imread(r"C:\Users\Connor\Desktop\network_ diagram\Switch.png")
    terminalImg = mpimg.imread(r"C:\Users\Connor\Desktop\network_ diagram\Terminal.png")
    
    #The for loop loops throught the tree nodes in linear order and uses the names and dType to
    #insert the correct image on the right node.
    for n in tree.nodes:
        
        #This gets all the position information about the image and places the axis to cover the position 
        #given to it
        (x,y) = pos[n.name]
        xx,yy = trans((x,y))
        xa,ya = trans2((xx,yy))
        a = plt.axes([xa - imsize/2.0, ya +.035 - imsize/2.0, imsize, imsize])
        
        #This block determines which image should be shown
        if(n.dType == 1):
            a.imshow(firewallImg)
        elif(n.dType == 2):
            a.imshow(interfaceImg)
        elif(n.dType == 3):
            a.imshow(terminalImg)
        elif(n.dType == 4):
            a.imshow(switchImg)
            
        #This displays the image
        a.set_aspect('equal')
        a.axis('off')
