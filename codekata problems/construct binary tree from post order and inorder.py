"""
LOGIC :
    INORDER TELLS THE VALUE IS GREATER OR LESSER
    POST ORDER TELLS THAT ROOT NODE IS THE LAST ELEMENT
"""
class binary_tree():
    global inorder
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,val):
        if inorder.index(self.data)>inorder.index(val):
            if self.left is None:
                self.left=binary_tree(val)
            else:
                self.left.add_child(val)
        if inorder.index(self.data)<inorder.index(val):
            if self.right is None:
                self.right=binary_tree(val)
            else:
                self.right.add_child(val)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

pre_order=[4,7,5,2,8,6,3,1]
inorder=[4,2,7,5,1,8,6,3]

root=binary_tree(1)

for i in range(len(pre_order)-2,-1,-1):
    root.add_child(pre_order[i])
print("completed adding child")

print("inorder traversal is")
print(root.in_order_traversal())

print("postorder traversal is")
print(root.post_order_traversal())