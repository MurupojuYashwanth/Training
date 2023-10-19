# DFS TRAVERSAL
#Pre-Order
#In-order
#Post_order

class node:
    def __init__(self,data):
        self.val=data
        self.left=Noned
        self.right=None
def traverse(root):
    if root==None:
        return
    print(root.val)  		#pre-order
    traverse(root.left)
                            #print(root.val)   #in-order
    traverse(root.right)
                            #print(root.val)   #post-order
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
traverse(root)