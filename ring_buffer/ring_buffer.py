class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # initalizes an empty list with a given capacity
        self.items = [None for i in range(capacity)]
        # initalizes index at zero for oldest value
        self.index = 0


    def append(self, item):
        # when index of oldest element is at capacity
        # set add the item 
        # set index back to zero
        if self.index == self.capacity - 1:
            self.items[self.index] = item
            self.index = 0

        # when index of oldest element is not at capacity
        # add the item
        # increase oldest index by 1
        else:
            self.items[self.index] = item 
            self.index += 1
        
    def get(self):
        # list comprehnsion that returns all values that are not None
        return [elem for elem in self.items if elem is not None]
        # print(self.index)


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.get() 
buffer.append('b')
buffer.get() 
buffer.append('c')
buffer.get() 

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
