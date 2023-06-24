class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end="")
                #temp.data means first nodes data
                temp=temp.next # establishing linked list
obj=singlelinkedlist()
# node creation - initialising
n=Node(10)# so n.data in node class will be 10
obj.head=n    #assigning first node as head
n1=Node(20)
obj.head.next=n1   # next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print("Inserting before 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_beginning(100)
obj.display()
print("")
print("After inserting 555")
obj.insert_beginning(555)
obj.display()