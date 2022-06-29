"""
SUMTREE IS A BINARY TREE WHERE VALUE OF NODE IS EQUAL TO SUM OF LEFT AND RIGHT NODE.
"""

class binary_tree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,val):
        if inorder.index(self.data) >inorder.index(val):
            if self.left is None:
                self.left=binary_tree(val)
            else:
                self.left.add_child(val)
        if inorder.index(self.data) <inorder.index(val):
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

    def sum_tree(self,target):
        left=0
        right=0

        if self.left:
            left=self.left.sum_tree(target)
        if self.right :
            right=self.right.sum_tree(target)
        if left==-1 or right==-1:
            return -1
        if left==0 and right==0:
            return self.data
        if left+right==self.data:
            if self.data==target:
                return True
            return self.data+left+right
        if self.data==target:
            return False
        return -1






if __name__=="__main__":
    root=binary_tree(26)
    root.left=binary_tree(10)
    root.right=binary_tree(3)

    root.left.left=binary_tree(4)
    root.left.right = binary_tree(6)

    root.right.right = binary_tree(3)

    print(root.sum_tree(root.data))