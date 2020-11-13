#Author : Jay Gohil

class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False
        self.predecessor = None

class BFS(object): #Breadth First Search

    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while (queue): #not empty

            actualNode = queue.pop()
            print(actualNode.name)

            for i in actualNode.adjacentList:
                if (i.visited == False):
                    i.visited = True
                    queue.append(i)


#Constructing Nodes
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

#Constructing Graph
node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)

bfs = BFS()
bfs.bfs(node1)
