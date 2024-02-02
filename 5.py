import uuid
import networkx as nx
import matplotlib.pyplot as plt


color_step_dfs = 20


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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

def dfs(node, visited, color_map, order):
    global color_step_dfs 
    if node is not None and node.id not in visited:
        visited.add(node.id)
        color = "#{:02X}{:02X}{:02X}".format(color_step_dfs, color_step_dfs, color_step_dfs)
        color_step_dfs += 15
        color_map[node.id] = color
        order.append((node.val, color))

        dfs(node.left, visited, color_map, order)
        dfs(node.right, visited, color_map, order)

def bfs(root, color_map, order):
    queue = [root]
    visited = set()
    color_step_bfs = 20  

    while queue:
        node = queue.pop(0)
        if node is not None and node.id not in visited:
            visited.add(node.id)
            color = "#{:02X}{:02X}{:02X}".format(color_step_bfs, color_step_bfs, color_step_bfs)
            color_step_bfs += 15
            color_map[node.id] = color
            order.append((node.val, color))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def visualize_tree(tree_root):
    tree_dfs = nx.DiGraph()
    pos_dfs = {tree_root.id: (0, 0)}
    tree_dfs = add_edges(tree_dfs, tree_root, pos_dfs)
    
    colors_dfs = {}
    order_dfs = []
    dfs(tree_root, set(), colors_dfs, order_dfs)
    
    tree_bfs = nx.DiGraph()
    pos_bfs = {tree_root.id: (0, 0)}
    tree_bfs = add_edges(tree_bfs, tree_root, pos_bfs)

    colors_bfs = {}
    order_bfs = []
    bfs(tree_root, colors_bfs, order_bfs)

    plt.figure(figsize=(16, 8))

    plt.subplot(1, 2, 1)
    nx.draw(tree_dfs, pos=pos_dfs, node_color=list(colors_dfs.values()), labels={node_id: str(tree_dfs.nodes[node_id]['label']) for node_id in tree_dfs.nodes}, with_labels=True, node_size=2500, font_size=10, font_color='white')
    plt.title('DFS обхід')
    print("DFS порядок обходу:\n", order_dfs)

    pos_bfs = {key: pos_bfs[key] for key in pos_bfs if key in colors_bfs}
    plt.subplot(1, 2, 2)
    nx.draw(tree_bfs, pos=pos_bfs, nodelist=list(colors_bfs.keys()), node_color=list(colors_bfs.values()), labels={node_id: str(tree_bfs.nodes[node_id]['label']) for node_id in tree_bfs.nodes if node_id in colors_bfs}, with_labels=True, node_size=2500, font_size=10, font_color='white')
    plt.title('BFS обхід')

    print("\nBFS порядок обходу:\n", order_bfs)

    plt.show()

# Создание дерева с большим количеством узлов
root_large = Node(0)
root_large.left = Node(1)
root_large.right = Node(2)
root_large.left.left = Node(3)
root_large.left.right = Node(4)
root_large.right.left = Node(5)
root_large.right.right = Node(6)
root_large.left.left.left = Node(7)
root_large.left.left.right = Node(8)
root_large.left.right.left = Node(9)
root_large.left.right.right = Node(10)
root_large.right.left.left = Node(11)
root_large.right.left.right = Node(12)
root_large.right.right.left = Node(13)
root_large.right.right.right = Node(14)

# Визуализация дерева с обходом в глубину и в ширину
visualize_tree(root_large)


