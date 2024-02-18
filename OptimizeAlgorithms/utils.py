from algorithm import *
import networkx as nx
import matplotlib.pyplot as plt
# Big O

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
print("Complexity of recursive_sum is O(n)")

def Visualize():
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    x = np.arange(1, 10, 0.1)
    y = np.log(x)
    plt.plot(x, y, label='O(log n)')
    y = x
    plt.plot(x, y, label='O(n)')
    y = x * np.log(x)
    plt.plot(x, y, label='O(n log n)')
    y = x ** 2
    plt.plot(x, y, label='O(n^2)')
    y = 2 ** x
    plt.plot(x, y, label='O(2^n)')
    plt.legend()
    plt.show()

def visualize_tree():
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_node(7)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(6, 7)
    nx.draw(G, with_labels=True)
    plt.show()

def sum_linked_list(linked_list):
    if linked_list.next is None:
        return linked_list.value
    else:
        return linked_list.value + sum_linked_list(linked_list.next)
    
def main():
    print(recursive_sum(10))
    linked_list = LinkedList(1)
    linked_list.next = LinkedList(2)
    linked_list.next.next = LinkedList(3)
    linked_list.next.next.next = LinkedList(4)
    linked_list.next.next.next.next = LinkedList(5)
    print(sum_linked_list(linked_list))

def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

def main2():
    print(reverse_string('hello'))
    print(reverse_string('world'))

def reverse_queue(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    return queue

def main3():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue = reverse_queue(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node is not None:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

def main4():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    in_order_traversal(root)
    pre_order_traversal(root)
    post_order_traversal(root)

def depth_first_search(node, value):
    visited = set()
    return depth_first_search_helper(node, value, visited)

def depth_first_search_helper(node, value, visited):
    if node.value == value:
        return True
    visited.add(node)
    for edge in node.edges:
        if edge not in visited:
            if depth_first_search_helper(edge, value, visited):
                return True
    return False

def main5():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node1.edges.append(node2)
    node2.edges.append(node3)
    node3.edges.append(node4)
    node4.edges.append(node5)
    print(depth_first_search(node1, 5))
    print(depth_first_search(node1, 6))

def main6():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)
    heap.insert(2)
    print(heap.extract_min())
    print(heap.extract_min())
    print(heap.extract_min())
    print(heap.extract_min())
    print(heap.extract_min())

def main7():
    trie = Trie()
    trie.insert('hello')
    trie.insert('world')
    print(trie.search('hello'))
    print(trie.search('world'))
    print(trie.search('hell'))
    print(trie.starts_with('he'))
    print(trie.starts_with('wor'))
    print(trie.starts_with('worl'))
    print(trie.starts_with('worlds'))

def is_valid_bst(node, min_value, max_value):
    if node is None:
        return True
    if node.value < min_value or node.value > max_value:
        return False
    return is_valid_bst(node.left, min_value, node.value) and is_valid_bst(node.right, node.value, max_value)

def main8():
    root = BinaryTreeNode(4)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(6)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)
    print(is_valid_bst(root, float('-inf'), float('inf')))
    root.right.left = BinaryTreeNode(8)
    print(is_valid_bst(root, float('-inf'), float('inf')))

def get_height(node):
    if node is None:
        return 0
    return node.height

def is_balanced(node):
    if node is None:
        return True
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

def main9():
    root = BalancedTreeNode(1)
    root.left = BalancedTreeNode(2)
    root.right = BalancedTreeNode(3)
    root.left.left = BalancedTreeNode(4)
    root.left.right = BalancedTreeNode(5)
    root.right.left = BalancedTreeNode(6)
    root.right.right = BalancedTreeNode(7)
    print(is_balanced(root))
    root.right.right.right = BalancedTreeNode(8)
    print(is_balanced(root))

def visualize_binary_tree():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_node(7)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(3, 7)
    nx.draw(G, with_labels=True)
    plt.show()

def visualize_multiway_tree():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_node(7)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(1, 5)
    G.add_edge(1, 6)
    G.add_edge(1, 7)
    nx.draw(G, with_labels=True)
    plt.show()

def visualize_graph():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_node(7)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(6, 7)
    nx.draw(G, with_labels=True)
    plt.show()

def visualize_circle():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)
    G.add_node(7)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(6, 7)
    G.add_edge(7, 1)
    nx.draw(G, with_labels=True)
    plt.show()

def visualize_graph2():
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.Graph()
        G.add_node(1)
        G.add_node(2)
        G.add_node(3)
        G.add_node(4)
        G.add_edge(1, 2, weight=10)
        G.add_edge(1, 3, weight=15)
        G.add_edge(1, 4, weight=20)
        G.add_edge(2, 3, weight=35)
        G.add_edge(2, 4, weight=25)
        G.add_edge(3, 4, weight=30)
        nx.draw(G, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=labels)
        plt.show()

def time(graph):
    import time
    start = time.time()
    tsp_solver = TSPSolver(graph)
    tsp_solver.solve()
    print(f'Time: {time.time() - start}')
    start = time.time()
    greedy_solver = GreedySolver(graph)
    greedy_solver.solve()
    print(f'Time: {time.time() - start}')
    start = time.time()
    dynamic_solver = DynamicSolver(graph)
    dynamic_solver.solve()
    print(f'Time: {time.time() - start}')
