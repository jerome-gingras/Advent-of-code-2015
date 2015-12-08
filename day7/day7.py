import re
global nodes
nodes = {}

class Node:
    def __init__(self, name, left, right, operator):
        self.value = 0
        self.isvalid = False
        self.name = name
        self.leftsource = left
        self.rightsource = right
        self.left = None
        self.right = None
        self.operator = operator
        
    def get_value(self):
        global nodes
        if self.isvalid:
            return self.value
        if self.leftsource.isdigit():
            self.left = int(self.leftsource)
        else:
            self.left = nodes[self.leftsource].get_value()
        if self.rightsource != None:
            if self.rightsource.isdigit():
                self.right = int(self.rightsource)
            else:
                self.right = nodes[self.rightsource].get_value()
        if self.operator == "SET":
            self.value = self.left
        elif self.operator == "NOT":
            self.value = (~self.left) & 65535
        elif self.operator == "LSHIFT":
            self.value = (self.left << self.right ) & 65535
        elif self.operator == "RSHIFT":
            self.value = self.left >> self.right
        elif self.operator == "OR":
            self.value = self.left | self.right
        elif self.operator == "AND":
            self.value = self.left & self.right
        self.isvalid = True
        return self.value

def create_node(line):
    wires = valuesRegex.findall(line)
    operator = operatorRegex.findall(line)
    destination = ''
    left = None
    right = None
    if len(operator) == 0:
        operator = "SET"
        destination = wires[1]
        left = wires[0]
    elif operator[0] == "NOT":
        operator = operator[0]
        destination = wires[1]
        left = wires[0]
    else:
        operator = operator[0]
        destination = wires[2]
        left = wires[0]
        right = wires[1]
    return Node(destination, left, right, operator)
    
f = open("input.txt", "r")
valuesRegex = re.compile("[a-z0-9]{1,}")
operatorRegex = re.compile("[A-Z]{2,}")
line = f.readline()

# Setup the node objects
while line != '':
    node = create_node(line)
    nodes[node.name] = node
    line = f.readline()
    
# Create the tree
a = nodes['a'].get_value()
print "Result part 1: " + str(a)

for key, node in nodes.iteritems():
    node.isvalid = False
    
nodes['b'].value = a
nodes['b'].isvalid = True

a = nodes['a'].get_value()
print "Result part 2: " + str(a)