import sys
import re
import string
import numpy 


class ArrayUtils():
    def _new_array(self, n: int, dtype=numpy.object):
        return numpy.empty(n, dtype)
    
    def _alloc_table(self, n: int, dtype=numpy.object):
        return [dtype() for _ in range(n)]
    

class BinaryHeap():

    def __init__(self):
        self.a = ArrayUtils()._new_array(10, dtype='<U6') #self.new_array(10,str)
        self.n = 0

    #def new_array(self, n, type):
        #a = numpy.empty(n, dtype=type)
        #for i in range(n):
            #a[i] = type()
        #return a

        ##temp = []
        ##for i in range(m):
            ##temp.append(0)
        ##self.a = temp

    def parent(self,i):
        return int((i-1)/2)

    def left(self,i):
        return int(2*i+1)

    def right(self,i):
        return int(2*(i+1))

    def add(self,x):
        #if self.a != None:
        if len(self.a) < self.n+1:
            print('Resizing')
            self.resize()
        self.a[self.n] = x
        self.n += 1
        #print(self.n)
        self.bubble_up(self.n-1)
        print(self.a)
        #print(type(self.a))
        x = 'here'
        #print(type(x))
        return True

    def bubble_up(self,i):
        p = self.parent(i)
        #print(i)
        while i>0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i] #swap i, p
            i = p
            p = self.parent(i)
        
    def remove(self):
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self.trickle_down(0)
        if 3*self.n < len(self.a):
            self.resize()
        return x

    def trickle_down(self,i):
        while i >= 0:
            j = -1
            r = self.right(i)
            if r<self.n and self.a[r] < self.a[i]:
                l = self.left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = self.left(i)
                if l<self.n and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                self.a[j], self.a[i] = self.a[i], self.a[j]
            i = j

    def resize(self):
        #if self.n > len(self.a):
        temp = ArrayUtils()._new_array(len(self.a)*2, dtype='<U6') #self.new_array(m, str)
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp
        #b = new_array(2*self.n)
        #b = self.a.copy()
        #self.a = b

    def is_empty(self):
        if self.n == 0:
            return True

bh = BinaryHeap()
bh.add('hi')
bh.add('6')
bh.add('7')
bh.add('1')
bh.add('try')
bh.add('trying')
bh.add('10')
bh.add('8')
bh.add('9')
bh.add('11')
bh.add('12')

'''
with open(mobydick.txt,'r') as f:
    for line in f:
        line = re.sub('[!#?,.:";\']', '', line).lower()
        token = line.split()
        for t in token:
            bh.add(t)
'''


