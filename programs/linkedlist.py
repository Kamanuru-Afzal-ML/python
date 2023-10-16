class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LikedList:
    def __init__(self):
        self.head=None
    def InsertAtbegining(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def InsertAtEnding(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next
        temp.next=new_node
    def Display(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
l=LikedList()
l.InsertAtbegining(1)
l.InsertAtbegining(1)
l.InsertAtbegining(1)
l.InsertAtEnding(90)
l.Display()