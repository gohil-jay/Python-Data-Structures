#Author : Jay Gohil

class Node(object):

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def insert(self, data):

        if (self.data == data):
            return False

        elif (self.data > data):
            if (self.left != None):
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            if (self.right != None):
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        while(current.left != None):
            current = current.left

        return current

    def maxValueNode(self, node):
        current = node

        while(current.right != None):
            current = current.right

        return current

    def countLeafNodes(self):
        if (self == None):
            return 0
        if ((self.left == None) and (self.right == None)):
            return 1
        else:
            return (self.left.countLeafNodes() + self.right.countLeafNodes())

    def delete(self, data):

        if (self == None): #no tree is there
            return None

        if (data < self.data): #data is there, but not same, so we traverse based on data value
            self.left = self.left.delete(data)

        elif (data > self.data): #data is there, but not same, so we traverse based on data value
            self.right = self.right.delete(data)

        else: #data is same, so we check whether it has one child only (using if and else), if it does, we do the below code
            if (self.left == None): #has only one child (right)
                temp = self.right
                self = None
                return temp
            else: #has only one child (left)
                temp = self.left
                self = None
                return temp

            #this will onlu run when 1. data is same | 2. node doesnt have only one child
            temp = self.minValueNode(self.roght)
            self.data = temp.data
            self.right = self.right.delete(temp.data) #recursion, doing above stuff again and again in case of two children

        return self

    def find(self, data):

        if (self.data == data):
            return True

        elif (data < self.data):
            if (self.left != None):
                return self.left.find(data)
            else:
                return False

        else:
            if (self.right != None):
                return self.right.find(data)
            else:
                return False

    def inorder(self):
        if (self != None):
            if (self.left != None):
                self.left.inorder()
            print(str(self.data), end = ' ')
            if (self.right != None):
                self.right.inorder()

    def postorder(self):
        if (self != None):
            if (self.left != None):
                self.left.postorder()
            if (self.right != None):
                self.right.postorder()
            print(str(self.data), end = ' ')

    def preorder(self):
        if (self != None):
            print(str(self.data), end = ' ')
            if (self.left != None):
                self.left.preorder()
            if (self.right != None):
                self.right.preorder()

    def find_predecessor_successor(self, data):

        global predecessor, successor
        predecessor = None
        successor = None

        if (self == None): #if no tree is there
            return False

        #Traversing till the given node.
        if (data < self.data):
            print("Moving Left.")
            self.left.find_predecessor_successor(data)

        if (data > self.data):
            print("Moving Right.")
            self.right.find_predecessor_successor(data)

        #Now finding the predecessor and successor of the node.
        if (self.data == data):

            if (self.left != None): #predecessor : turn left, and then right till you can
                temp = self.left #takes value of left node,

                if (temp.right != None): #check if it has right node
                    while(temp.right != None): #go right until it can
                        temp = temp.right
                
                predecessor = temp #give final value to global predecessor variable

            if (self.right != None): #predecessor : turn right, and then left till you can
                temp = self.right #takes value of right node,

                if (temp.left != None): #check if it has left node
                    while(temp.left != None): #go left until it can
                        temp = temp.left
                
                successor = temp #give final value to global successor variable

        return

    def path(self, data):
        if (data < self.data):
            print("Moving Left.")
            self.left.path(data)

        if (data > self.data):
            print("Moving Right.")
            self.right.path(data)

        if (self.data == data):
            print("Found!")
            return True

    def height(self):
        try: #keep recursing (traversing down) untill last node comes
            return (1 + max(self.left.height(), self.right.height())) #keep checking and comparing down and down.
        except:
            return 0 #the self.right.height() is actually 'None.height()' which throws error, so in that case, we return 0.

    def balance(self):
        if (self == None):
            return 0
        return ((self.left.height()) - (self.right.height()))

    def rotateLeft(self):

        tempLeft = self.left
        t = tempLeft.right

        tempLeft.right = self
        self.left = t

        return tempLeft

    def rotateRight(self):

        tempRight = self.right
        t = tempRight.left

        tempRight.left = self
        self.right = t

        return tempRight

class AVL_Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if (self.root != None):
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def countLeafNode(self):
        print()
        print("Number of leaf Nodes : ")
        print(self.root.countLeafNodes())

    def delete(self, data):
        if (self.root != None):
            return self.root.delete(data)
        else:
            return False

    def find(self, data):
        if (self.root != None):
            return self.root.find(data)
        else:
            return False

    def path_node(self, data):
        print()
        print("Path : ")
        return self.root.path(data)

    def find_pre_succ(self, data):
        print()
        self.root.find_predecessor_successor(data)

    def height(self):
        return self.root.height()

    def inorder(self):
        if (self.root != None):
            print()
            print("Inorder : ")
            self.root.inorder()
        else:
            return False

    def postorder(self):
        if (self.root != None):
            print()
            print("Postorder : ")
            self.root.postorder()
        else:
            return False

    def preorder(self):
        if (self.root != None):
            print()
            print("Preorder : ")
            self.root.preorder()
        else:
            return False

"""
if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))

    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
    print()
    print("----------------------")
"""


if __name__ == '__main__':
    root = Tree()
    root.insert(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    root.insert(55)
    root.insert(75)
    root.insert(65)
    root.insert(85)

    # following BST is created
    #               50
    #            /      \
    #           30        70
    #          /  \     /    \
    #        20   40  60     80
    #                /  \   /  \
    #               55  65 75  85

    root.find_pre_succ(70)
    if  (predecessor is not None) and (successor is not None):
        print('Predecessor:', predecessor.data, 'Successor:', successor.data)
    else:
        print('Predecessor:', predecessor, 'Successor:', successor)

    root.countLeafNode()
    print()
    print()
    root.path_node(75)
    print()
    print("The height of the BST is : ", root.height())
    print()
