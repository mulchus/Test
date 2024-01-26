from collections import deque

"""
Алгоритм поиска в ширину (BFS) используется для обхода или поиска в графе. Он начинает с выбора стартовой вершины и пошагово распространяется по всем смежным вершинам.

Шаги алгоритма:
1. Создается пустое множество visited для отслеживания посещенных вершин и очередь queue для управления порядком обхода.
2. Стартовая вершина добавляется в очередь и отмечается как посещенная.
3. Пока очередь не пуста, извлекается вершина из начала очереди (queue.popleft()).
4. Выводится значение текущей вершины и добавляются в очередь все её смежные вершины, которые еще не были посещены.
5. Шаги 3-4 повторяются до тех пор, пока очередь не опустеет.

Сложность:
Временная сложность: O(V + E), где V — количество вершин, E — количество ребер в графе.
Пространственная сложность: O(V), так как используется множество для отслеживания посещенных вершин.
"""

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
