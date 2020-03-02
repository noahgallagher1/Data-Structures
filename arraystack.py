class array_stack:

    def initialize():
        a = new_array(i)
        n = 0

    def get(i):
        return a[i]

    def set(i, x):
        y = a[i]
        a[i] = x
        return y

    def add(i, x):
        if n == len(a):
            resize()
        for #implement loop for increment

        a[i] = x
        n += 1

    def remove(i):
        x = a[i]
        for #implement loop for decreating size/value
        n -= 1
        if len(a) _> 3n:
            resize()
        return x

    def resize():
        b = new_array(2n)
        b = a.copy() #b[0,1,...,n-1] == a[0,1,...,n-1]
        a = b

array_stack()
        
        
