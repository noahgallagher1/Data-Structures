class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None
        self.recover = 0


class DLList:

    def __init__(self):
        self.n = 0
        self.dummy = Node(None)
        dummy = self.dummy
        dummy.prev = self.dummy
        dummy.next = self.dummy

    def size(self):
        return(self.n)
    
    def get_node(self,i):
        if i < (self.n/2):
            p = self.dummy.next
            for j in range(0,i):
                p = p.next
        else:
            p = self.dummy
            for j in range(0,(self.n - i)):
                p = p.prev
                
        return p

    def get(self,i):
        return self.get_node(i) #.item .x

    def set(self,i,x):
        u = self.get_node(i)
        y = u.x
        u.x = x 
        return y

    def add_before(self,w,x):
        u = Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1 
        return u

    def add(self,i,x):
        self.add_before(self.get_node(i),x)

    def _remove(self,w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1 
        return(w.item)
    
    def remove(self):
        return(self._remove(self.get_node(0)))

    def printList(self, l):
        print ('\nTranversal in Forward Direction:')
        l = self.dummy.next
        while (l is not self.dummy):
            print(l.item, end = " ")
            last = l
            l = last.next
    
    def returnList(self,l):
        l = self.dummy.next
        while(l is not self.dummy):
            return(l.item)
            last = l
            l = last.next
    
    def append(self,x):
        self.add_before(self.get_node(self.n-1),x)
            
    
        




#d = DLList()
#d.add(1,1)
#d.add(2,2)
#d.add(3,7)
#d.add(4,9)
#d.printList(d.dummy)



       
