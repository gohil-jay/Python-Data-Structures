# Author : Jay Gohil

# Algorithm for Heaps

import sys
import heapq

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

    def __omp__(self, otherVertex):
        return self.omp(self.minDis, otherVertex.minDis)

    def __it__(self, other):
        selfPriority = self.minSelf
        otherPriority = other.minSelf
        return (selfPriority < otherPriority)


class Algo(object):

    def calShortPath(self, startVertex, vertexList):

        heap = []
        startVertex.minDis = 0
        heapq.heappush(heap, startVertex)

        while (len(heap) > 0):

            actualvertex = heapq.heappop(heap)

            for edge in actualvertex.adjacentList:

                i = edge.startVertex
                j = edge.targetVertex
                newDis = i.minDis + edge.weight

                if (newDis < j.minDis):
                    j.predecessor = i
                    j.minDis = newDis
                    heapq.heappush(heap, j)

    def getShortPath(self, targetVertex):

        print("The shortest path is : ", targetVertex.minDis)

        node = targetVertex

        while (node != None):
            print(node.name)
            node = node.predecessor

#-------------------------------------------------------------------

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

algo = Algo()
algo.calShortPath(node1, vertexList)
algo.getShortPath(node7)
