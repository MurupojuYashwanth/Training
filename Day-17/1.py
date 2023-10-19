class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class ll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_begin(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def insert_end(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=temp
    def traverse_front(self):
        if self.head==None:
            print("No Nodes available")
        else:
            temp=self.head
            while temp!=None:
                print(temp.val)
                temp=temp.next
    def traverse_reverse(self):
        if self.tail==None:
            print("No nodes")
        else:
            temp=self.tail
            while temp!=None:
                print(temp.val)
                temp=temp.prev
    
l=[5,4,3,2,1]
o1=ll()
for i in l:
    o1.insert_begin(i)
o1.insert_end(6)
#o1.traverse_front()
o1.traverse_reverse()

