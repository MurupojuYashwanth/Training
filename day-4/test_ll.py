class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            self.head.next=node(x)
b = cse()
b.creat(20)
b.creat(30)
print(b.head.data)