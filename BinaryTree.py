import FIFOQueue

class Node():
    def __init__(self,x):
        self.x = x #=item

        self.next = None
        self.prev = None
        self.parent = None

        self.left = None
        self.right = None
        self.t = self.x


class Tree():

    def __init__(self):
        self.r = None
        self.n = 0
        
    def depth(self,u):
        d = 0
        while(u is not self.r):
            u = u.parent
            d += 1
        return(d)
        
    def size(self,u):
        if u is None:
            return 0
        return(1+size(u.left)+size(u.right))

    def height(self, u):
        if u is None:
            return 0
        return(1+max(self.height(u.left),self.height(u.right)))

    def traverse(self,u): #with recursion
        if u is None:
            return 0
        self.traverse(u.left)
        print(u.x)
        self.traverse(u.right)
        #print(u.x)

    def traverse_without_recursion(self,u):
        u = self.r
        prev = None
        while u is not None:
            if prev == u.parent:
                if u.left is not None:
                    next = u.left
                    #print(u.x)
                elif u.right is not None:
                    next = u.right
                    print(u.x)
                else:
                    next = u.parent
                    print(u.x)
            elif prev == u.left:
                if u.right is not None:
                    next = u.right
                    print(u.x)
                else:
                    next = u.parent                    
            else:
                next = u.parent               
            prev = u
            u = next
        
    def size(self):
        u = r
        prev = None
        n = 0
        while u is not None:
            if prev == u.parent:
                n += 1
                if u.left is not None:
                    next = u.left
                elif u.right is not None:
                    next = u.right
                else:
                    next = u.parent
            elif prev == u.left:
                if u.right is not None:
                    next = u.right
                else:
                    next = u.parent
            else:
                next = u.parent
            prev = u
            u = next
        return n

    
    def BF_traverse(self):
        q = FIFOQueue.FIFO_Queue() #import FIFO queue
        q.append(self.r)
        while(q.size()>0):
            u = q.pop() 
            if u.left is not None:
                q.append(u.left)
            if u.right is not None:
                q.append(u.right)
        #print(q.show())

    
    def find_eq(self,x):
        w = self.r
        while(w is not None):
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        return None

    def find(self,x):
        z = None
        w = self.r
        while(w is not None):
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z == None:
            return None
        return(z.x)
        
    def add(self,x):
        p = self.first_last(x)
        return self.add_child(p,Node(x)) 

    def first_last(self,x):
        w = self.r
        prev = None
        while(w is not None):
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def add_child(self,p,u):
        w = self.r
        if p == None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    
    def splice(self,u):
        if u.left is not None:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s is not None:
            s.parent = p
        self.n -= 1

    def remove_node(self,u):#find smallest number greater than u
        if u.left is None or u.right is None:
            splice(u)
        else:
            w = u.right
            while (w.left is not None): 
                w = w.left
            u.x = w.x
            self.splice(w)

    def order_traversal(self,u):
        if u.left is not None:
            order_traversal(u.left)
        print(u.x)
        if u.right is not None:
            order_traversal(u.right)



tr = Tree()
tr.add(7)
tr.add(5)
tr.add(3)
tr.add(8)
tr.add(9)
tr.add(1)
tr.add(4)
tr.add(9)
tr.add(2)
tr.add(6)

print(tr.traverse(tr.r))
print(tr.traverse_without_recursion(tr.r))
print(tr.height(tr.r))   
print(tr.depth(tr.find(9)))
print(tr.depth(tr.find(5)))
print(tr.depth(tr.find(4)))
tr.splice(tr.find(5))
print(tr.depth(tr.find(4)))
print(tr.height(tr.r))

