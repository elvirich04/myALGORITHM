class LinkedListNode:
    def __init__(self,data):
        self.data=data
        self.tail=None
    def SetHead(self,node):
        node.tail=self
    def SetTail(self,node):
        self.tail=node
        
def TraverseLinkedList(Node):
    while Node!=None:
        print(Node.data)
        Node=Node.tail

Node1=LinkedListNode("Angel Locsin")
Node2=LinkedListNode("Piolo Pascual")
Node3=LinkedListNode("Katrina Halili")
Node4=LinkedListNode("Myrtelle")
Node5=LinkedListNode("Coco Martin")

Node5.SetTail(Node1)
Node1.SetTail(Node4)
Node4.SetTail(Node2)
Node2.SetTail(Node3)
#Node3.SetTail(Node5)

TraverseLinkedList(Node5)
