#Author: Jay Gohil

class Node(object):

    def __init__(self, data, next = None, prev = None):
        self.data = data;
        self.next = next;
        self.prev = prev;
        
    def setData(self, data):
        self.data = data;
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev
        
    def getPrev(self):
        return self.next
    
class LinkedList(object):

    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def printReverse(self): #here, we only print in back order, not change the actual linkedList
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        while (temp.prev != None):
            print(temp.data)
            temp = temp.prev
            
    def insertAtStart(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertBetween(self, prev_node, data):
        if (prev_node.next == None):
            print("The previous node must have a next and previous node.")
            print()
        else:
            newNode = Node(data)
            
            newNode.next = prev_node.next
            newNode.prev = prev_node
            prev_node.next.prev = newNode
            prev_node.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def length(self):
        count= 0
        temp = self.head
        while (temp != None):
            count += 1
            temp = temp.next

        print("The Length of LinkedList is : ", count)

    def delete(self, data):

        temp = self.head

        if (temp.next != None):
            if (temp.data == data):
                self.head = temp.next
                self.head.prev = None
                temp = None
                return
            else:
                while (temp.next != None): #traverse till we have the node and its previous node
                    if (temp.data == data):
                        break
                    previous = temp
                    temp = temp.next

                if temp == None:
                    return

                previous.next = temp.next
                temp.next.prev = previous
                return

    def search(self, node, data): #finds node by recursion
        if node == None:
            return False
        elif (node.data == data):
            return True
        return self.search(node.getNext(), data)

    def reverse(self): #this is awesome but hard in doubly, we have easier method, without changing the actual LinkedList
        previous = None
        current = self.head

        while (current != None):
            temp = current.next
            current.next = previous
            if (previous != None):
                previous.prev = current
            previous = current
            current = temp
        self.head = previous

"""
if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)
    node2 = Node(2)
    List.head.setNext(node2)
    node3 = Node(3)
    node2.setNext(node3)
    List.insertAtStart(4)
    List.insertBetween(node2, 5)
    List.insertAtEnd(6)
    List.printLinkedList()
    print()
    List.delete(5)
    List.printLinkedList()
    print()
    List.length()
    print()
    print(List.search(List.head, 4))
"""

""" For Checking the reverse function"""
if __name__ == '__main__':
    myLinkedList = LinkedList()
    for i in range(10, 0, -1):
        myLinkedList.insertAtStart(i)

    print('Original:')
    myLinkedList.printLinkedList()
    print()
    print('Reversed:')
    myLinkedList.printReverse()
