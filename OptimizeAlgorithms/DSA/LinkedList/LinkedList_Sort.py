import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values):
        self.head = None
        self.nodes = []
        for value in values:
            self.append(value)

    def append(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next
                yield self.to_list(), (current.value if current else None, current.next.value if current and current.next else None)

class LinkedListSort:
    def __init__(self, ll):
        self.ll = ll
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Linked List Sorting')
        self.positions = list(range(len(self.ll.to_list())))
        self.sc = self.ax.scatter(self.positions, self.ll.to_list(), c='blue')
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.iteration = 0
        self.time = 0
        self.start_time = time.time()
        self.anim = None

    def update_plot(self, frame):
        values, swapped = frame
        self.sc.set_offsets(list(zip(self.positions, values)))
        colors = ['red' if value in swapped else 'blue' for value in values]
        self.sc.set_color(colors)
        self.iteration += 1
        self.time = time.time() - self.start_time
        self.text.set_text(f'Iterations: {self.iteration}\nTime: {self.time:.2f} s')
        return self.sc,

    def animate(self, frames):
        self.anim = animation.FuncAnimation(self.fig, self.update_plot, frames=frames, repeat=False, blit=False, interval=50)
        plt.xlabel('Linked List Nodes')
        plt.ylabel('Values')
        plt.show()

    def start(self):
        frames = list(self.ll.bubble_sort())
        self.animate(frames)

    def save(self, filename):
        self.anim.save(filename, writer='imagemagick')

def main():
    values = [random.randint(1, 50) for _ in range(10)]
    ll = LinkedList(values)
    ll_sort = LinkedListSort(ll)
    ll_sort.start()
    ll_sort.save('linked_list_sort.gif')

if __name__ == '__main__':
    main()
