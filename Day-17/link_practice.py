class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
    def insert_end(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
    def traverse(self):
        if self.head==None:
            print("No Nodes available")
        else:
            temp=self.head
            while temp!=None:
                print(temp.val)
                temp=temp.next
    
l=[5,4,3,2,1]
o1=ll()
for i in l:
    o1.insert_begin(i)
o1.insert_end(6)
o1.traverse()