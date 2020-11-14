#Author: Jay Gohil
#Isnt working properly, needs debugging

import sys

class edge(object):

    def __init__(self, weight, startVertex, targetVertex):

        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacentList = []
        self.minDis = sys.maxsize #infinite

class BellmanFord(object):

    has_Cycle = False

    def calShortPath(self, vertexList, edgeList, startVertex):

        startVertex.minDis = 0

        for i in range(0, len(vertexList)-1):
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetVertex

                newDis = u.minDis + edge.weight

                if (newDis < v.minDis):
                    v.minDis = newDis
                    v.predecessor = u

        for edge in edgeList:
            if (self.hasCycle(edge) == True):
                print("Negative cycle detected ..")
                BellmanFord.has_Cycle = True
                return

    def hasCycle(self, edge):
        if ((edge.startVertex.minDis + edge.weight) < (edge.targetVertex.minDis)):
            return True
        else:
            return False

    def getShortPath(self, targetVertex):
        if (BellmanFord.hasCycle != True):
            print("Shortest path : ")

            node = targetVertex

            while (node != None):
                print(node.name)
                node = node.predecessor

        else:
            print("Negative Cycle Detected ..")


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = edge(5,node1, node2)
edge2 = edge(8,node1, node8)
edge3 = edge(9,node1, node5)
edge4 = edge(15,node2, node4)
edge5 = edge(12,node2, node3)
edge6 = edge(4,node2, node8)
edge7 = edge(7,node8, node3)
edge8 = edge(6,node8, node6)
edge9 = edge(5,node5, node8)
edge10 = edge(4,node5, node6)
edge11 = edge(20,node5, node7)
edge12 = edge(1,node6, node3)
edge13 = edge(13,node6, node7)
edge14 = edge(3,node3, node4)
edge15 = edge(11,node3, node7)
edge16 = edge(9,node4, node7)

node1.adjacentList.append(edge1)
node1.adjacentList.append(edge2)
node1.adjacentList.append(edge3)
node2.adjacentList.append(edge4)
node2.adjacentList.append(edge5)
node2.adjacentList.append(edge6)
node8.adjacentList.append(edge7)
node8.adjacentList.append(edge8)
node5.adjacentList.append(edge9)
node5.adjacentList.append(edge10)
node5.adjacentList.append(edge11)
node6.adjacentList.append(edge12)
node6.adjacentList.append(edge13)
node3.adjacentList.append(edge14)
node3.adjacentList.append(edge15)
node4.adjacentList.append(edge16)

vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)
edgeList = (edge2, edge2, edge3, edge4, edge5, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16)

algo = BellmanFord()
algo.calShortPath(vertexList, edgeList, node7)
algo.getShortPath(node7)
