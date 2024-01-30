import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap(arr):
    heapq.heapify(arr)
    return [HeapNode(key) for key in arr]

def visualize_heap(heap):
    heap_graph = nx.Graph()
    pos = {}

    level_height = 6  # Висота рівня відстані між рівнями
    current_level = 1

    for i, node in enumerate(heap, start=1):
        heap_graph.add_node(node.id, color=node.color, label=node.key)
        pos[node.id] = (i, -current_level * level_height)

        if i > 1:
            parent_index = i // 2
            heap_graph.add_edge(heap[parent_index - 1].id, node.id)

        # Змінюємо рівень для нащадків
        if i % 2 == 0:
            current_level += 1

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=True, node_size=2500, node_color=colors, with_labels=True)
    plt.show()

# Приклад використання:
arr = [4, 10, 3, 5, 1]
heap = build_heap(arr)
print (arr)
visualize_heap(heap)