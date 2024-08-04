import heapq

# Клас для представлення графа
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Якщо граф неорієнтований

# Клас для представлення мін-купи
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, node):
        heapq.heappush(self.heap, node)
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0

# Алгоритм Дейкстри
def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.V)}
    D[start_vertex] = 0
    
    min_heap = MinHeap()
    min_heap.push((0, start_vertex))  # (вага, вершина)
    
    while not min_heap.is_empty():
        (dist, current_vertex) = min_heap.pop()
        
        for neighbor, weight in graph.graph[current_vertex]:
            distance = dist + weight
            
            if distance < D[neighbor]:
                D[neighbor] = distance
                min_heap.push((distance, neighbor))
    
    return D

# Приклад використання
def main():
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    
    distances = dijkstra(g, 0)
    
    for vertex in range(len(distances)):
        print(f"Відстань від вершини 0 до вершини {vertex}: {distances[vertex]}")

if __name__ == "__main__":
    main()
