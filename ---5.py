# import uuid
# import networkx as nx
# import matplotlib.pyplot as plt

# class Node:
#     def __init__(self, key, color="skyblue"):
#         self.left = None
#         self.right = None
#         self.val = key
#         self.color = color
#         self.id = str(uuid.uuid4())

# def add_edges(graph, node, pos, x=0, y=0, layer=1):
#     if node is not None:
#         graph.add_node(node.id, color=node.color, label=node.val)
#         if node.left:
#             graph.add_edge(node.id, node.left.id)
#             l = x - 1 / 2 ** layer
#             pos[node.left.id] = (l, y - 1)
#             l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
#         if node.right:
#             graph.add_edge(node.id, node.right.id)
#             r = x + 1 / 2 ** layer
#             pos[node.right.id] = (r, y - 1)
#             r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
#     return graph

# def draw_tree(tree_root, title="Binary Tree"):
#     tree = nx.DiGraph()
#     pos = {tree_root.id: (0, 0)}
#     tree = add_edges(tree, tree_root, pos)

#     colors = [node[1]['color'] for node in tree.nodes(data=True)]
#     labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

#     plt.figure(figsize=(8, 8))
#     nx.draw_circular(tree, labels=labels, arrows=True, node_size=2500, node_color=colors, with_labels=True)
#     plt.title(title)
#     plt.show()

# def reset_colors(node):
#     if node is not None:
#         node.color = "skyblue"
#         reset_colors(node.left)
#         reset_colors(node.right)

# def depth_first_traversal(node, depth=0):
#     if node is not None:
#         node.color = color_for_depth(depth)
#         print(f"Visited node {node.val} with color {node.color}")
#         depth_first_traversal(node.left, depth + 1)
#         depth_first_traversal(node.right, depth + 1)

# def breadth_first_traversal(root):
#     if root is None:
#         return

#     queue = [root]
#     depth = 0

#     while queue:
#         current_level = []
#         for node in queue:
#             node.color = color_for_depth(depth)
#             print(f"Visited node {node.val} with color {node.color}")
#             if node.left:
#                 current_level.append(node.left)
#             if node.right:
#                 current_level.append(node.right)

#         queue = current_level
#         depth += 1

# def color_for_depth(depth):
#     intensity = 255 - depth * 20
#     color = "#{:02X}{:02X}{:02X}".format(intensity, intensity, 255)
#     return color

# # Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

# # Обходи та відображення
# print("\nDepth-First Traversal:")
# depth_first_traversal(root)
# draw_tree(root, title="Depth-First Traversal")

# # Скидуємо колір для наступного обходу
# reset_colors(root)

# # Створення дерева для обходу в ширину
# root_bfs = Node(0)
# root_bfs.left = Node(4)
# root_bfs.left.left = Node(5)
# root_bfs.left.right = Node(10)
# root_bfs.right = Node(1)
# root_bfs.right.left = Node(3)

# print("\nBreadth-First Traversal:")
# breadth_first_traversal(root_bfs)
# draw_tree(root_bfs, title="Breadth-First Traversal")


import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_traversal(node, depth=0):
    if node is not None:
        node.color = color_for_depth(depth)
        print(f"Visited node {node.val} with color {node.color}")
        depth_first_traversal(node.left, depth + 1)
        depth_first_traversal(node.right, depth + 1)

def breadth_first_traversal(root):
    if root is None:
        return

    queue = [root]
    depth = 0

    while queue:
        current_level = []
        for node in queue:
            node.color = color_for_depth(depth)
            print(f"Visited node {node.val} with color {node.color}")
            if node.left:
                current_level.append(node.left)
            if node.right:
                current_level.append(node.right)

        queue = current_level
        depth += 1

def color_for_depth(depth):
    # Генерація кольорів від темних до світлих
    intensity = 255 - depth * 20
    color = "#{:02X}{:02X}{:02X}".format(intensity, intensity, 255)
    return color

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обходи та відображення
print("\nDepth-First Traversal:")
depth_first_traversal(root)

print("\nBreadth-First Traversal:")
breadth_first_traversal(root)

# Відображення дерева після обходів
draw_tree(root)