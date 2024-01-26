from collections import deque


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges):
        self.vertices[vertex] = edges
        print(self.vertices)
        
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            curent_vertex = queue.popleft()
            print(curent_vertex, end=" ")
            
            for neighbor in self.vertices[curent_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# пример использования
graph = Graph()
graph.add_vertex("A", ["B", "C"])
graph.add_vertex("B", ["A", "D", "E"])
graph.add_vertex("C", ["A", "F", "G"])
graph.add_vertex("D", ["B"])
graph.add_vertex("E", ["B", "H"])
graph.add_vertex("F", ["C"])
graph.add_vertex("G", ["C"])
graph.add_vertex("H", ["E"])

print('Обход графа в ширину (BFS): ')
graph.bfs("A")
