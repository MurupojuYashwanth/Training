class node:
    def __init__(self,z):
        self.data = z 
        self.next = None
class list1:
    def __init__(self):
        self.head = None
    def create(self,x):
        if self.head == None:
            self.head = node(x)
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = node(x)
    def addfront(self,x):
        if self.head == None:
            self.head = node(x)
        else:
            temp = node(x)
            temp.next = self.head
            self.head = temp
    def traverse(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next
a = list1()
a.create(10)
a.addfront(20)
a.addfront(30)
a.create(40)
a.traverse()