# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        This method adds a new vertex to the graph.
        """
        self.v_count += 1
        self.adj_matrix = [[0 for x in range(self.v_count)]for y in range(self.v_count)]
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        This method adds a new edge to the graph.
        """
        if src > self.v_count-1 or dst > self.v_count-1:
            return
        if self.adj_matrix[src] and self.adj_matrix[dst] and weight > 0 and src != dst:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        This method removes an edge between two vertices
        """
        if src < 0 or dst < 0:
            return
        if src > self.v_count - 1 or dst > self.v_count - 1:
            return
        if self.adj_matrix[src] and self.adj_matrix[src][dst] > 0:
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        This method returns a list of vertices of the graph
        """
        verts =[]

        for i in range(self.v_count):
            verts.append(i)
        return verts

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph
        """
        eds = []
        for x in range(self.v_count):
            for y in range(self.v_count):
                if self.adj_matrix[x][y] > 0:
                    eds.append((x, y, self.adj_matrix[x][y]))
        return eds

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        eds = []
        k = 0
        for x in range(self.v_count):
            for y in range(self.v_count):
                if self.adj_matrix[x][y] > 0:
                    eds.append((x, y))

        while k+1 < len(path):
            if (path[k], path[k+1]) in eds:
                k += 1
            else:
                return False
        return True

    def dfs(self, v_start, v_end=None, visited=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in ascending order
        """
        if v_end is not None:
            if not self.adj_matrix[v_start][v_end]:
                v_end = None

        if visited is None:
            visited = []

        if v_start < 0 or v_start > self.v_count -1:
            return visited
        visited.append(v_start)

        adj = self.adj_matrix[v_start]
        for x in range(self.v_count):
            if adj[x] > 0 and x not in visited and v_end not in visited:
                self.dfs(x, v_end, visited)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in ascending order
        """
        visited = []
        queue = [v_start]
        if v_start < 0 or v_start > self.v_count - 1:
            return visited
        while queue and v_end not in visited:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
                adj = self.adj_matrix[v]
                for x in range(self.v_count):
                    if adj[x] > 0 and x not in visited and v_end not in visited:
                        queue.append(x)
        return visited

    def has_cycle(self):
        v_start = 0

        if self.rec_has_cycle(v_start):
            return True
        return False

    def rec_has_cycle(self, v_start, parent=None, visited=None):
        """
        TODO: Write this implementation
        """
        if visited is None:
            visited = []
        visited.append(v_start)

        adj = self.adj_matrix[v_start]

        for x in range(self.v_count):
            if adj[x] > 0 and x not in visited:
                if self.rec_has_cycle(x, v_start, visited):
                    return True
            return True
        return False

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
