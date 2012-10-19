class Tree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo=cargo
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.cargo)
left=Tree(2)
right=Tree(3)
tree=Tree(1,left,right)
def total(tree):
    if tree==None:
        return 0
    return (total(tree.left)+total(tree.right)+(tree.cargo))
def print_tree(tree):
    if tree==None:
        return
    print (tree.cargo, print_tree(tree.left), print_tree(tree.right))
def print_tree_postorder(tree):
    if tree==None:
        return
print_tree_postorder(tree.left)
print_tree_postorder(tree.right)
print (tree.cargo)
def print_tree_inorder(tree):
    if tree==None:
        return
print_tree_inorder(tree.left)
print (tree.cargo)
print_tree_inorder
