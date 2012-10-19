class node:
    parent = None
    left = None
    right = None
    key = None
    data = None
    	     
    def __init__(self, key, data):
        self.key = key
        self.data = data
     
class binary_tree:
    root = None
    __count = 0
	     
    def __follow(self, key):
        current = self.root
        trail = []
        value = isinstance(key, node) and key.key or key
             
        while True:
            if current == None:
                break
                 
            trail.append(current)
           
            if value == current.key:
                break
            elif value < current.key:
                current = current.left
            elif value > current.key:
                current = current.right
            else:
                # ok...?
                break
    	         
        return (trail)
    	     
    def find(self, key):
        value = isinstance(key, node) and key.key or key
        trail = self.__follow(value)
       
        if trail == []:
            return
          
        if trail[-1].key == value:
            return (trail[-1])
      
    def insert(self, key, data):
        trail = self.__follow(key)
           
        if trail == []:
            self.root = node(key, data)
            self.__count += 1
            return
    	         
        if key == trail[-1].key:
            return
        elif key < trail[-1].key:
            trail[-1].left = node(key, data)
            trail[-1].left.parent = trail[-1]
            self.__count += 1
            return (trail[-1].left)
        elif key > trail[-1].key:
            trail[-1].right = node(key, data)
            trail[-1].right.parent = trail[-1]
            self.__count += 1
            return (trail[-1].right)
         
    def delete(self, key):
        value = isinstance(key, node) and key.key or key
        trail = self.__follow(value)
       
        if trail == []:
            return False
         
        if value != trail[-1].key:
            return False
          
        if (trail[-1].left == None) and (trail[-1].right == None):
            if trail[-1].parent == None:
                self.root = None
            else:
                if value < trail[-1].parent.key:
                    trail[-1].parent.left = None
                elif value > trail[-1].parent.key:
                    trail[-1].parent.right = None
        elif trail[-1].left == None:
            if trail[-1].parent == None:
                self.root = trail[-1].right
                self.root.parent = None
            else:
                if value < trail[-1].parent.key:
                    trail[-1].parent.left = trail[-1].right
                    trail[-1].parent.left.parent = trail[-1].parent
                elif value > trail[-1].parent.key:
                    trail[-1].parent.right = trail[-1].right
                    trail[-1].parent.right.parent = trail[-1].parent
        elif trail[-1].right == None:
            if trail[-1].parent == None:
                self.root = trail[-1].left
                self.root.parent = None
            else:
                if value < trail[-1].parent.key:
                    trail[-1].parent.left = trail[-1].left
                    trail[-1].parent.left.parent = trail[-1].parent
                elif value > trail[-1].parent.key:
                    trail[-1].parent.right = trail[-1].left
                    trail[-1].parent.right.parent = trail[-1].parent
        else:
            temp = trail[-1].left
          
            while temp.right != None:
                temp = temp.right
                 
            tempdata = temp.data           
            tempkey = temp.key
            self.delete(temp)
            trail[-1].data = tempdata
            trail[-1].key = tempkey
            
        self.__count -= 1
       
    def depth(self, node):
        if node == None:
            return (0)
        else:
            leftdepth = self.depth(node.left)
            rightdepth = self.depth(node.right)
         
            return (max(leftdepth, rightdepth) + 1)
    
    def min(self, node):
        while node.left != None:
            node = node.left
      
        return (node)
      
    def max(self, node):
        while node.right != None:
            node = node.right
      
        return (node)
       
    def listkeys(self, node):
        l = []
         
        if node.left != None:
            l.extend(self.listkeys(node.left))
        
        if node.key != None:
            l.append(node.key)
      
        if node.right != None:
            l.extend(self.listkeys(node.right))
        
        return(l)
         
    def listdata(self, node):
        l = []
             
        if node.left != None:
            l.extend(self.listdata(node.left))
    
        if node.data != None:
            l.append(node.data)
      
        if node.right != None:
            l.extend(self.listdata(node.right))
         
        return (l)
      
    def listnodes(self, node):
        l = []
     
        if node.left != None:
            l.extend(self.listnodes(node.left))
       
            l.append(node)
      
        if node.right != None:
            l.extend(self.listnodes(node.right))
      
        return (l)
    
    def formattree(self, node, indentsize = 2, indent = 0):
        string = ""
       
        if node == None:
            return ""
         
        string += (indent * " ") + str(node.key) + ": " + str(node.data) 
       
        if node.left != None:
            string += self.formattree(node.left, indentsize, indent + indentsize)
       
        if node.right != None:
            string += self.formattree(node.right, indentsize, indent + indentsize)
      
        return (string)
      
    def __len__(self):
        return (self.__count)
     
    def __getitem__(self, key):
        item = self.find(key)
        
        if item != None:
            return (item.data)
     
    def __setitem__(self, key, data):
        item = self.find(key)
         
        if item == None:
            item = self.insert(key, data)
        else:
            item.data = data
       
    def __delitem__(self, key):
        self.delete(key)
     
    def __contains__(self, key):
        item = self.find(key)
      
        return (item != None)
    
    def __str__(self):
         return ("binary_tree with " + str(self.__count) + " nodes\\n" + self.formattree(self.root))
     
    def __repr__(self):
        return (str(self))
     
    def __eq__(self, other):
        if not isinstance(other, binary_tree):
            return False
       
        selfkeylist = self.listkeys(self.root)
        selfdatalist = self.listdata(self.root)
        otherkeylist = other.listkeys(other.root)
        otherdatalist = other.listdata(other.root)
    
        return ((selfkeylist == otherkeylist) and (selfdatalist == otherdatalist))
     
    def __ne__(self, other):
        return not (self == other)
     
def test_binary_tree(tree):
    import random
      
    times = 100
    r = random.SystemRandom()
     
    while times != 0:
        times -=(1)
        
        tree[r.randint(0, 10000)] = 0
     
    print (tree.formattree(tree.root))
    
# test program if this file is run
if __name__ == "__main__" :
    test_binary_tree(binary_tree())

#from binary_tree import binary_tree
tree = binary_tree()
# add some items
tree["abc"] = "one"
tree["xyz"] = "two"
tree["hello"] = "three"
# print a (sorted) list of keys in the tree
print (tree.listkeys(tree.root))
# print a formatted tree of the tree
print (tree.formattree(tree.root))
#delete a node
del (tree["abc"])
