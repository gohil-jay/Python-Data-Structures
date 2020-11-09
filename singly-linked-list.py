#Author: Jay Gohil

class Node(object):

    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;
        
    def setData(self, data):
        self.data = data;
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
class LinkedList(object):

    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertBetween(delf, prev_node, data):
        if (prev_node.next == None):
            print("The previous node must have a next node.")
            print()
        else:
            newNode = Node(data)
            newNode.next = prev_node.next
            prev_node.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode

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
                temp = None
                return
            else:
                while (temp.next != None): #traverse till we have the node and its previous node
                    if (temp.data == data):
                        break
                    prev = temp
                    temp = temp.next

                if temp == None:
                    return

                prev.next = temp.next
                return

    def search(self, node, data): #finds node by recursion
        if node == None:
            return False
        elif (node.data == data):
            return True
        return self.search(node.getNext(), data)

    def reverse(self):#this is awesome (do in notebook)
        prev = None
        current = self.head

        while (current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev


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
    List.delete(3)
    List.printLinkedList()
    print()
    List.length()
    print()
    print(List.search(List.head, 1))
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
    myLinkedList.reverse()
    myLinkedList.printLinkedList()
