class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class list:
    def __init__(self):
        self.head=None
    def create(self,x):
        if self.head==None:
            self.head=node(x)
            self.next=None 
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(x)
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
a=list()
a.create(10)
a.create(20)
a.addfront(30)
a.display()