class FIFO_Queue:
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

    def append(self, item):
        self.array.append(item)
        if self.n > len(self.array):
            resize()
        self.n += 1

    def pop(self):
        self.n -= 1
        return self.array.pop(0)

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

        
s = FIFO_Queue()
s.append('1')
s.append('2')
print(s.pop())
print(s.show())
