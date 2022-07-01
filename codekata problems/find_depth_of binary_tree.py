class binary_tree():

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,val):
        if self.data>val:
            if self.left is None:
                self.left=binary_tree(val)
            else:
                self.left.add_child(val)
        if self.data<val:
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



def depth(val):
    if not (val.left or val.right):
        return 0

    left = 0
    right = 0

    if val.left:
        left = depth(val.left)

    if val.right:
        right = depth(val.right)

    maxi = max(left, right) + 1

    return maxi


if __name__=="__main__":
    arr = [[17, 4, 20, 9, 1, 18, 23, 34],[1],[1,2,3],[5,3,4,2,1],[5,4,3,2,1]]  #contruct binary tree from array
    for testcase in arr:
        root = binary_tree(testcase[0])      # first element as root

        for i in range(1, len(testcase)):
            root.add_child(testcase[i])

        print("THE ARRAY IS ",testcase)
        print("THE DEPTH OF BINARY TREE IS ",depth(root))
        print("-" * 40)