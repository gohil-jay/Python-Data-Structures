#Author: Jay Gohil

class Queue(object):

    def __init__(self, limit):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return (self.queue == [])

    def enqueue(self, data):
        if (self.size >= self.limit):
            return -1
        else:
            self.queue.append(data)

        if (self.front == None):
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

    def dequeue(self):
        if (self.isEmpty()):
            return -1
        else:
            self.queue.pop(0)
            self.size -= 1 #this is queue

            if (self.size == 0):
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1

    def getSize(self):
        return self.size

    def priority_delete(self): #delete elemts first based on priority (large number = hugher priority)
            max = 0
            for i in range(len(self.queue)):
                if (self.queue[i] > self.queue[max]):
                    max = i

            item = self.queue[max]
            del self.queue[max]
            return item

if __name__ == '__main__':

    myQueue = Queue(20)

    for i in range(10):
        myQueue.enqueue(i)

    print(myQueue)
    print('Queue Size:',myQueue.getSize())

    myQueue.dequeue()
    myQueue.enqueue(39)
    myQueue.enqueue(3000)

    print(myQueue)
    print('Queue Size:',myQueue.getSize())
    
    while not myQueue.isEmpty(): #removing all elements based on priority
        print(myQueue.priority_delete(), end = ' ')

    print()
    print('Queue Size:',myQueue.getSize())
