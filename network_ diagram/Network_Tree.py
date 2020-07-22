"""
By: Connor Shabro

Description:
This file holds the class code for the tree and node. This is used to 
hold the cvs file info so that the graph is easier to create. It also
utilizes a linear list of the nodes so that find can be linear time.
"""

"""
Description of Tree class:
The tree class is utilized to allow a faster add connection function when creating the graph.
It also has a linear list of the nodes so that it can have a faster find time since it 
is not sorted.
"""
class Tree:
    
    """
    Description of __init__:
    This is the intilation for Tree objects which pulls the information from the list
    that holds the csv information
    """
    def __init__(self, network):
        #dType is a number that represents what image should be used for the device.
        dType = self.findDType(network[0][3])
        self.root = self.Node(network[0][0], network[0][1], network[0][2], dType)
        self.nodes = []
        self.start = 0
        self.tracker = 0
        
        #This is a linear list of the nodes so that find is faster
        self.nodes.append(self.root)
        
        #This starts the creation of the tree
        self.build_tree(network, 0, 1)
        
    """
    Description of build_tree:
    This is the algorithm that fills the tree structure using the csv information. 
    The parents keep a list of their children nodes which allows for descent through
    the tree.
    """
    def build_tree(self, network, level, row):
        #This is for if there was no information given
        if(row >= len(network)):
            return
        
        #This is a check to see if it needs to go to the next row before starting
        if(network[row][0] == "-"):
            self.start = len(self.nodes) - self.tracker - 1
            self.build_tree(network, level + 1, row + 1)
        else:
            #Until it hits the - which indicates a new level it loops through the devices.
            while(network[row][0] != "-"):
                #This fills in the information for the node
                dType = self.findDType(network[row][3])
                cur = self.Node(network[row][0], network[row][1], network[row][2], dType)
                self.nodes.append(cur)
                self.tracker += 1
                #This adds the connection to the parent node with the new node
                self.add_connection(cur)
                row += 1
                if(row >= len(network)):
                    return
                    
            #start is a class variable that tracks where it should start searching
            #for the parent node to save time
            self.start = len(self.nodes) - self.tracker - 1
            
            #recursively calls the function to build the tree
            self.build_tree(network, level + 1, row + 1)
     
    """
    Description of add_connection:
    This first looks through the node list starting from start 
    and looks for the parent and once it finds it it appends it to
    the connections of the parent.
    """           
    def add_connection(self, cur):
        #Starts from start and will look till the end
        for i in range(self.start, len(self.nodes) - 1):
            #If the name matches it adds it to connection
            if(cur.parent == self.nodes[i].name):
                self.nodes[i].connections.append(cur)
                break
    
    """
    Description of print_tree:
    This prints off the linear list of nodes since that saves space compared
    to printing it off recursively.
    """
    def print_tree(self):
        #Loops through the nodes and prints the names of the nodes.
        for i in range(len(self.nodes)):
            print(self.nodes[i].name)
      
    """
    Description of findDtype:
    It compares the string given by the csv to see what type of device it is
    and returns a number that allows for easy image insertion based off of this.
    """  
    def findDType(self, typeOfDevice):
        #These are the types of devices currently supported to get photos.
        if(typeOfDevice == 'Firewall'):
            return 1
        elif(typeOfDevice == 'Interface'):
            return 2
        elif(typeOfDevice == 'Terminal'):
            return 3
        elif(typeOfDevice == 'Switch'):
            return 4
        #If the name didn't match it returns a 0 which is no photo
        else:
            return 0
                    
    """
    Description of Node class:
    Node class is used by the tree class which will hold the data for each device and connections
    that the nodes have to other ones. 
    """
    class Node:
    
        """
        Description of __init__:
        This fills in the data for nodes upon creation. Connections only get filled after the 
        node is created.
        """
        def __init__(self, name, ip, connection, deviceType):
            #Inserts data based on info given through parameters.
            self.name = name
            self.parent = connection    
            self.connections = []
            self.IP = ip
            self.dType = deviceType
        
        """
        Description of print_info function:
        This prints out all the information fields in the node object
        """
        def print_info(self):
            print("Name: " + self.name)
            print("Parent: " + self.parent)
            print("ip: " + str(self.IP))
            print("Connections:")
            
            #This loops through the nodes connections and prints off their names
            for i in range(len(self.connections) - 1):
                print(self.connections[i].name)
        
        

