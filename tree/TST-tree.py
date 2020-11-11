class Node(object):

    def __init__(self, character):

        self.character = character
        self.left = None
        self.right = None
        self.mid = None
        self.value = 0

class TST(object):

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.insertItem(self.root, key, value, 0)

    def insertItem(self, node, key, value, index):

        c = key[index]

        if (node == None):
            node = Node(c)

        if (c < node.character):
            node.left = self.insertItem(node.left, key, value, index)

        elif (c > node.character):
            node.right = self.insertItem(node.right, key, value, index)

        elif (index < (len(key)-1)):
            node.mid = self.insertItem(node.mid, key, value, (index+1))

        else:
            node.value = value

        return node

    def get(self, key):

        node = self.getItem(self.root, key, 0)

        if (node == None):
            return -1

        return node.value

    def getItem(self, node, key, index):

        if (node == None):
            return None

        c = key[index]

        if (c < node.character):
            return self.getItem(node.left, key, index)

        elif (c > node.character):
            return self.getItem(node.right, key, index)

        elif (index < (len(key)-1)):
            return self.getItem(node.mid, key, (index+1))
        else:
            return node

if __name__ == "__main__":

    tst = TST()

    tst.insert("apple", 2)
    tst.insert("banana", 4)
    tst.insert("orange", 37)

    print(tst.get("orange"))
