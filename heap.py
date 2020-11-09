#Author: Jay Gohil

class heap(object):

    heap_size = 10

    def __init__(self):
        self.heap = [0]*(heap_size)
        self.currentPos = -1

    def __repr__(self):
        heap = self.heap[1:]
        return ' '.join(str(i) for i in heap)

    def insert(self, item):

        if (self.isFull() == true):
            print("Heap full !!")
            return

        self.currentPos += 1
        self.heap[currentPos] = item
        self.fixUP(self.cuurentPos)

    def fixUP(self, position):
        
        while (position // 2) > 0: #keep interating to parent nodes

            if self.heap[position] < self.heap[position // 2]:  #if upper is smaller than lower, SWAP

                temp = self.heap[position // 2]
                self.heap[position // 2] = self.heap[position]
                self.heap[position] = temp

            position = position // 2

    def heapSort(self):
        
        for i in range(0, (self.currentPos + 1)):
            temp = self.heap[0]
            self.heap[0] = self.heap[self.currentPos - i]
            self.heap[self.currentPos - i] = temp

            self.fixDOWN(0, (currentPos - i - 1))

    def fixDOWN(self, position, upto):

        while (position <= upto):

            left = ((2*position) + 1)
            right = ((2*position) + 2)

            if (left < upto):
                child_to_swap = None

                if (right > upto):
                    child_to_swap = left
                else:
                    if (self.heap[left] > self.heap[right]):
                        child_to_swap = left
                    else:
                        child_to_swap = right

                if (self.heap[position] < self.heap[child_to_swap]:
                    temp = self.heap[position]
                    self.heap[position] = self.heap[child_to_swap]
                    self.heap[child_to_swap] = temp
                else:
                    break

                position = child_to_swap

            else:
                break

    def isFull(self):
        if (self.currentPos == Heap.heap_size):
            return true
        else:
            return False
    


"""
from heapq import heappush, heappop, heapify

heap = []
nums = [12,3,-2,6,4,8,9]
x = nums

for num in nums:
    heappush(heap, num)

print(heap)

heapify(x)

print(x)
"""
