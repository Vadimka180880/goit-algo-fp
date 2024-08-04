import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас для представлення вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Функція для додавання ребер до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Додавання вузла до графа
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Додавання ребра до лівого вузла
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Додавання ребра до правого вузла
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Клас для реалізації мін-купу
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)  # Додавання елемента до купи
        self.heapify_up(len(self.heap) - 1)  # Відновлення властивості мін-купу знизу вверх

    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.heapify_up(parent_index)  # Рекурсивно піднімаємося по дереву

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Якщо залишився один елемент, просто видаляємо його
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Замінюємо корінь останнім елементом
        self.heapify_down(0)  # Відновлення властивості мін-купу зверху вниз
        return root

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)  # Рекурсивно опускаємося по дереву

# Функція для побудови дерева з мін-купу
def build_tree_from_heap(heap):
    if not heap:
        return None
    nodes = [Node(key) for key in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]  # Призначаємо лівого нащадка
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]  # Призначаємо правого нащадка
    return nodes[0]  # Повертаємо корінь дерева

# Функція для візуалізації мін-купу
def visualize_heap(heap):
    root = build_tree_from_heap(heap)
    draw_tree(root)

# Основна функція
def main():
    min_heap = MinHeap()
    elements = [10, 4, 5, 30, 3, 1, 8, 12, 6]  # Елементи для додавання до мін-купу
    for element in elements:
        min_heap.insert(element)
    
    print("Мін-купа:", min_heap.heap)
    visualize_heap(min_heap.heap)  # Візуалізація мін-купу

if __name__ == "__main__":
    main()
