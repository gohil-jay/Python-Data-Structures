#Author : Jay Gohil

class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacentList = []
        self.visited = False
        self.predecessor = None

class DFS(object): #Depth First Search

    def dfs(self, node):

        node.visited = True
        print(node.name)

        for i in node.adjacentList:
            if (i.visited == False):
                self.dfs(i)


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

print("----------------------------------")

dfs = DFS()
dfs.dfs(node1)
