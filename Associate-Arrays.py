class hashTable(object):

    def __init__(self):
        self.size = 10
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def insert(self, key, value):

        index = self.hashFunction(key)

        while (self.keys[index] != None):

            if (self.keys[index] == key):
                self.values[index] = data #Update
                return

            index = ((index + 1)%(self.size))

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):

        index = self.hashFunction(key) #get the index of key

        while (self.keys[index] != None): #check until found it

            if (self.keys[index] == key):
                return self.values[index]

            index = ((index + 1)% (self.size))

        return None #return none if not found.

    def hashFunction(self, key): #own hash function, there can be many

        # Add the ASCII values of all digits
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])

        #get the sum in the range of table's size.
        return ((sum)%(self.size))

if __name__ == "__main__":

    table = hashTable()
    table.insert('abc', 2)
    table.insert('pqr', 4)
    table.insert('xyz', 7)

    print(table.get('abc'))
