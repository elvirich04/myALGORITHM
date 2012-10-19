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

Node1=LinkedListNode("Vice President")
Node2=LinkedListNode("President")
Node3=LinkedListNode("Treasurer")
Node4=LinkedListNode("Secretary")

Node2.SetTail(Node1)
Node1.SetTail(Node4)
Node4.SetTail(Node3)

TraverseLinkedList(Node2)
