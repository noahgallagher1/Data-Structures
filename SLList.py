class SLList():
    def __init__(self):
        self.n = 0
        self.head = None
        self.Tail = None

    def add(self,i,x):
        if i > self.n:
            resize()
        u = new_node(i,x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def get(self,i):
        for l in node:
            if l == i:
                return(i)

    def remove(self,i):
        for l in node:
            if l == i:
                node.pop(i)
