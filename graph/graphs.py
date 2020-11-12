# Author : Jay Gohil

class Graph():

    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def BFS(self, startVertex):
        # Take a list for stoting already visited vertexes
        visited = [False] * len(self.vertex)

        # create a list to store all the vertexes for BFS
        queue = []

        # mark the source node as visited and enqueue it
        visited[startVertex] = True
        queue.append(startVertex)

        while queue:
            startVertex = queue.pop(0)
            print(startVertex, end = ' ')

            # mark all adjacent nodes as visited and print them
            for i in self.vertex[startVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self):
        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end = ' ')

        # Recur for all the vertexes that are adjacent to this node
        for i in self.vertex.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)

    # This function will return True if graph is cyclic else return False
    def checkCyclic(self):
        visited = [False] * len(self.vertex)
        stack = [False] * len(self.vertex)
        for vertex in range(len(self.vertex)):
            if visited[vertex] == False:
                if self.checkCyclicRec(visited, stack, vertex) == True:
                    return True
        return False

    # Recursive function for finding the cycle
    def checkCyclicRec(self, visited, stack, vertex):
        # Mark the current node in visited and also add it to the stack
        visited[vertex] = True
        stack[vertex] = True

        # mark all adjacent nodes of the current node
        for adjacentNode in self.vertex[vertex]:
            if visited[adjacentNode] == False:
                if self.checkCyclicRec(visited, stack, adjacentNode) == True:
                    return True
            elif stack[adjacentNode] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        stack[vertex] = False
        return False

    def topologicalSort(self):
        visited = [False] * self.count           # Marking all vertices as not visited
        stack = []                               # Stack for storing the vertex
        for vertex in range(self.count):
            # Call the recursive function only if not visited
            if visited[vertex] == False:
                self.topologicalSortRec(vertex, visited, stack)

        print(' '.join([str(i) for i in stack]))
        # print(stack)

    # Recursive function for topological Sort
    def topologicalSortRec(self, vertex, visited, stack):

        # Mark the current node in visited
        visited[vertex] = True

        # mark all adjacent nodes of the current node
        try:
            for adjacentNode in self.vertex[vertex]:
                if visited[adjacentNode] == False:
                    self.topologicalSortRec(adjacentNode, visited, stack)
        except KeyError:
            return

        # Push current vertex to stack which stores the result
        stack.insert(0,vertex)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print('BFS:')
    g.BFS(2)
    print('DFS:')
    g.DFS()
