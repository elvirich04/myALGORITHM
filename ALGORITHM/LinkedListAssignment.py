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

Node1=LinkedListNode("Nokia C3")
Node2=LinkedListNode("Nokia 5110")
Node3=LinkedListNode("Nokia 1100")
Node4=LinkedListNode("Samsung Galaxy Y")
Node5=LinkedListNode("Nokia X201")
Node6=LinkedListNode("Nokia 3310")


Node2.SetTail(Node6)
Node6.SetTail(Node3)
Node3.SetTail(Node1)
Node1.SetTail(Node5)
Node5.SetTail(Node4)

TraverseLinkedList(Node2)
