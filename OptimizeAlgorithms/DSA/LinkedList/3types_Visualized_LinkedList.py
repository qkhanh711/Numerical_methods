import pydot

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Tạo một danh sách liên kết đơn giản
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Tạo đồ thị
graph = pydot.Dot(graph_type='digraph')

# Thêm các node vào đồ thị
current = node1
while current:
    node = pydot.Node(str(id(current)), label=str(current.value))
    graph.add_node(node)
    if current.next:
        edge = pydot.Edge(str(id(current)), str(id(current.next)))
        graph.add_edge(edge)
    current = current.next

# Lưu và hiển thị đồ thị
graph.write_png('linked_list.png')
graph.write_pdf('linked_list.pdf')

import networkx as nx
import matplotlib.pyplot as plt

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Tạo một danh sách liên kết đơn giản
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Tạo đồ thị
G = nx.DiGraph()

# Thêm các node và các cạnh vào đồ thị
current = node1
while current:
    G.add_node(current.value)
    if current.next:
        G.add_edge(current.value, current.next.value)
    current = current.next

# Vẽ đồ thị
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=16, font_color="black", font_weight="bold", arrowsize=20)
plt.show()

from graphviz import Digraph

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Tạo một danh sách liên kết đơn giản
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Tạo đối tượng đồ thị
dot = Digraph()

# Thêm các node vào đồ thị
current = node1
while current:
    dot.node(str(id(current)), str(current.value))
    if current.next:
        dot.edge(str(id(current)), str(id(current.next)))
    current = current.next

# Hiển thị đồ thị
dot.render('linked_list', format='png', view=True)
