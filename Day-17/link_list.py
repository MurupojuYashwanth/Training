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
    def delete_begin(self):
        if self.head==None:
            print("No nodes available")
        else:
            temp=self.head
            self.head=temp.next
            #self.head=self.head.next
    def delete_end(self):
        if self.head==None:
            print("No nodes available")
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def traverse(self):
        temp=self.head
        while temp!=None:
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
o=ll()
for i in l:
    o.insert_begin(i)
o.insert_end(20)
o.delete_begin()
o.delete_end()
o.traverse()







'''
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)
#o2=node(2)
#o3=node(3)
#o1.next=o2
#o2.next=o3
#print(o1.val,o1.next.val,o1.next.next.val)'''