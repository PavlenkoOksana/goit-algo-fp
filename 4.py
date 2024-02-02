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
   
    level_height = 1  # Висота рівня, відстані між рівнями
    current_level = 1

    for i, node in enumerate(heap, start=1):
        heap_graph.add_node(node.id, color=node.color, label=node.key)
        
        if i > 1:
            parent_index = i // 2
            x_offset = -1/current_level**2 if i % 2 == 0 else 1/current_level**2
            
            # Оновлення координати x для батька, якщо він ще не має значення
            parent_id = heap[parent_index - 1].id
            parent_x, parent_y = pos.get(parent_id, (0, -1))
            pos[parent_id] = (parent_x, parent_y)
            
            pos[node.id] = (parent_x + x_offset, -current_level * level_height)
            heap_graph.add_edge(parent_id, node.id)

        # Змінюємо рівень для нащадків
        if (i + 1) % (2**(current_level-1)) == 0:
            current_level += 1


    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=True, node_size=1500, node_color=colors, with_labels=True)
    plt.show()

#arr = [4, 10, 3, 5, 1]
arr = [4, 10, 3, 5, 1, 12, 14, 15, 16, 18, 22, 20, 24, 2]
heap = build_heap(arr)
print("Купа:")
for node in heap:
    print(node.key, end=", ")
print("\n")
visualize_heap(heap)