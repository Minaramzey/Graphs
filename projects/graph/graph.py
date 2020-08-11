"""
Simple graph implementation 
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Verwx Does Not Exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        queue = Queue()
        queue.enqueue(starting_vertex)
        #   Create an empty Set to store visited vertices
        visited = set()
        #   While the queue is not empty
        while queue.size() > 0:
            #   dequeue the first vertex
            v = queue.dequeue()
            #   If that vertex has not been visted...
            if v not in visited:
                #   mark it as visited
                print(v)
                visited.add(v)
                # all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    queue.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        stack = Stack()
        # 2. Push on our starting node
        stack.push(starting_vertex)
        # 3. Make a set to track if we've been here before (so we don't go there twice)
        visited = set()
        # 4. While our stack isn't empty, 
        while stack.size() > 0:
        # 5. Pop off whatever's on top, this is our current
            current = stack.pop()
            if current not in visited:
                print(current)
        # 6. If we haven't visited this vertex yet, then mark as Visited
            if current not in visited:
                    visited.add(current)
        # 8. Get it's neighbors
                    neighbors = self.get_neighbors(current)    
        # 9. For each of the neighbors, add to the stack
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.push(neighbor)
                            
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for value in self.vertices[starting_vertex]:
            if value not in visited:
                self.dft_recursive(value, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        visited = set()
        #   Queue will hold a tuple (currentVertex, path)
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            #   Split queue into vertex and path
            path = queue.dequeue()
            vertex = path[-1]
            #   If vertex has not been visited or if it the starting_vertex
            if vertex not in visited:
                #   Add vertex to visited
                visited.add(vertex)
                #   If it is the vertex we are looking for return the path
                if vertex == destination_vertex:
                    return path
                #   Add neighbors to stack
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(path + [neighbor])
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current = stack.pop()
            visited.add(current)

            for vertex in self.get_neighbors(current):
                if vertex not in visited:
                    stack.push(vertex)
                if vertex is destination_vertex:
                    visited.add(vertex)
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited={}):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited[starting_vertex] = [starting_vertex]

        neighbors = self.get_neighbors(starting_vertex)
        if len(neighbors) > 0:
            for n in neighbors:
                if n not in visited:
                    visited[n] = visited[starting_vertex] + [n]

                    if n == destination_vertex:
                        return visited[n]
                    else:
                        dfs_check = self.dfs_recursive(n, destination_vertex, visited)
                        if dfs_check is not None:
                            return dfs_check
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
