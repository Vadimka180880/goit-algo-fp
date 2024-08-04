import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Клас для представлення вузла дерева
class Node:
    def __init__(self, key, color="#FFFFFF"):  # Початковий колір - білий
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
def draw_tree(tree_root, ax):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    ax.clear()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

# Функція для зміни кольору вузла
def update_node_color(node, step, total_steps, color_type='blue'):
    shade = int((step / total_steps) * 225)
    hex_shade = f'{shade:02X}'
    if color_type == 'blue':
        node.color = f'#88ff{hex_shade}'  # Відтінки зеленого
    elif color_type == 'yellow':
        node.color = f'#ffff{hex_shade}'  # Відтінки жовтого

# Обхід в глибину (ітеративний)
def depth_first_search(root):
    if root is None:
        return []

    stack = [root]
    step = 0
    total_steps = count_nodes(root)
    traversal = []

    while stack:
        node = stack.pop()
        update_node_color(node, step, total_steps, 'blue')
        step += 1
        traversal.append(copy_tree(root))  # Додаємо копію дерева до обходу
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return traversal

# Обхід в ширину (ітеративний)
def breadth_first_search(root):
    if root is None:
        return []

    queue = [root]
    step = 0
    total_steps = count_nodes(root)
    traversal = []

    while queue:
        node = queue.pop(0)
        update_node_color(node, step, total_steps, 'yellow')
        step += 1
        traversal.append(copy_tree(root))  # Додаємо копію дерева до обходу
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return traversal

# Функція для копіювання дерева
def copy_tree(node):
    if node is None:
        return None
    new_node = Node(node.val, node.color)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    return new_node

# Функція для підрахунку кількості вузлів у дереві
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Анімація обходу дерева
def animate_traversal(traversal, interval=1000):
    fig, ax = plt.subplots()

    def update(num):
        draw_tree(traversal[num], ax)

    ani = animation.FuncAnimation(fig, update, frames=len(traversal), repeat=False, interval=interval)
    plt.show()

# Основна функція
def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print("Обхід в глибину:")
    dfs_traversal = depth_first_search(root)
    animate_traversal(dfs_traversal)

    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print("Обхід в ширину:")
    bfs_traversal = breadth_first_search(root)
    animate_traversal(bfs_traversal)

if __name__ == "__main__":
    main()
