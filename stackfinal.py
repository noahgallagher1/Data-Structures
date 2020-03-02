class my_stack:

    def __init__(self):
        self.array = []
        self.n = 0
        

    def new_array(self, m):
        temp = []
        for i in range(m):
            temp.append(0)
        self.array = temp


    def isEmpty(self):
        return self.size() == 0
        
    def push(self, item):
        self.array.append(item)
        if self.n > len(self.array):
            resize()
        self.n += 1

    def pop(self):
        self.n -= 1
        return self.array.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty")
        return self.array[-1]

    def size(self):
        return len(self.array)

    def show(self):
        return self.array


    def resize(self):
        if self.n > len(self.array):
            temp = new_array(m)
            for i in range(self.n):
                temp[i] = self.array[i]
            self.array = temp

        
s = my_stack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())


