import math
class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linked_list():
    def __init__(self):
        self.parent=None
        self.length=0
    def add_at_last(self,data):
        self.length+=1
        if self.parent is None:
            self.parent=Node(data,None)
        else:
            itr=self.parent
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None)
    def print_list(self):
        itr=self.parent
        while itr:
            print(itr.data,"->",end=" ")
            itr=itr.next
    def middle_element(self):
        if self.length<3:
            print(self.parent.data)
        else:
            middle=math.ceil(self.length/2)
            itr=self.parent
            for i in range(middle-1):
                itr=itr.next
            print(itr.data)


obj=Linked_list()
arr=list(map(int,input("enter the space seperated array ").split()))
for i in arr:
    obj.add_at_last(i)
print("printing linked list")
obj.print_list()
print("\nMIDDLE ELEMENT IS ",end="  ")
obj.middle_element()