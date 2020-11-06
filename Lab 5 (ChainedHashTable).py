import random
import Lab4
class ChainedHashTable:

    def __init__(self):
        self.d = 1
        self.t = self.allocate_table(2^(self.d))
        self.z = 2*(random.randint(1,100))+1  #random odd int btw 1 & 100, step by 2
        self.n = 0
        self.array = []
        self.w = 60

    def allocate_table(self, m):
        temp = []
        for i in range(m):
            temp.append(Lab4.DLList()) #0 is not right, implement DLL?
        self.array = temp


    def add(self,x):
        if self.find(x) is not None:
            return False
        if (self.n + 1) > len(self.t):
            resize()
        #if t[hash(x)] is None:
            #t[hash(x) = 
        self.t[hash(x)].append(x)
        n += 1
        return True

    def remove(self,x):
        l = self.t[hash(x)]
        for y in l:
            if y == x:
                l.remove(y)
                self.n -= 1
                if (3*n) < len(t):
                    resize()
                return y
        return None

    def find(self,x):
        for y in self.t[self.hash(x)]:
            if y == x:
                return y
        return None


    def resize(self):
        d += 1
        temp = allocate_table(2^(d-1))
        for i in [0,2^(d-1)]:
            temp[i]=t[i]
        t = allocate_table(2^d)
        for i in [0,2^(d-1)]:
            if temp[i] is not None:
                print(d)#transverse list and add

    def hash(self,x):
        print((self.z)*x)
        return (((self.z)*(x))%(2^(self.w)) / (2^((self.w)-(self.d))))
            
HM = ChainedHashTable()
HM.add((0,1))

