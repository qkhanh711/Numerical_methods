import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Sort:
    def __init__(self, arr, highlight = False):
        self.original_arr = arr.copy()
        self.arr = arr.copy()
        self.n = len(arr)
        self.fig, self.ax = plt.subplots()
        self.ax.set_title(f'Sorting, {highlight}')
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align='edge')
        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.iteration = 0
        self.time = 0
        self.start_time = time.time()
        self.anim = None
        self.alg_name = None
        self.algs = {
            'Bubble Sort': self.bubble_sort,
            'Selection Sort': self.selection_sort,
            'Insertion Sort': self.insertion_sort,
            'Merge Sort': self.merge_sort,
            'Quick Sort': self.quick_sort,
            'Heap Sort': self.heap_sort
        }
        self.highlight = highlight

    def update_plot(self, frame):
        arr, swapped = frame
        for rect, val in zip(self.bar_rects, arr):
            rect.set_height(val)
            if self.highlight:
                if rect.get_x() in swapped:
                    rect.set_color('tomato')
                else:
                    rect.set_color('skyblue')
        self.iteration += 1
        self.time = time.time() - self.start_time
        self.text.set_text(f'Iterations: {self.iteration}\nTime: {self.time:.2f} s')
        return self.bar_rects

    def animate(self, frames):
        self.anim = animation.FuncAnimation(self.fig, self.update_plot, frames=frames, repeat=False, blit=False, interval=50)
        plt.xlabel(f'{self.alg_name}')
        # plt.show()

    def reset_array(self):
        self.arr = self.original_arr.copy()
        self.iteration = 0
        self.time = 0
        self.start_time = time.time()

    def bubble_sort(self):
        frames = []
        for i in range(self.n):
            for j in range(self.n - i - 1):
                swapped = set()
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped.add(j)
                    swapped.add(j + 1)
                frames.append((self.arr.copy(), swapped))
        return frames

    def selection_sort(self):
        frames = []
        for i in range(self.n):
            min_index = i
            for j in range(i + 1, self.n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            swapped = {i, min_index}
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            frames.append((self.arr.copy(), swapped))
        return frames

    def insertion_sort(self):
        frames = []
        for i in range(1, self.n):
            key_item = self.arr[i]
            j = i - 1
            swapped = set()
            while j >= 0 and self.arr[j] > key_item:
                self.arr[j + 1] = self.arr[j]
                swapped.add(j)
                swapped.add(j + 1)
                j -= 1
            self.arr[j + 1] = key_item
            frames.append((self.arr.copy(), swapped))
        return frames

    def merge_sort(self):
        frames = []
        def merge(arr, start, mid, end):
            left = arr[start:mid + 1]
            right = arr[mid + 1:end + 1]
            k = start
            swapped = set()
            while left and right:
                if left[0] <= right[0]:
                    arr[k] = left.pop(0)
                else:
                    arr[k] = right.pop(0)
                swapped.add(k)
                k += 1
                frames.append((arr.copy(), swapped))
            while left:
                arr[k] = left.pop(0)
                swapped.add(k)
                k += 1
                frames.append((arr.copy(), swapped))
            while right:
                arr[k] = right.pop(0)
                swapped.add(k)
                k += 1
                frames.append((arr.copy(), swapped))

        def merge_sort_alg(arr, start, end):
            if start < end:
                mid = (start + end) // 2
                merge_sort_alg(arr, start, mid)
                merge_sort_alg(arr, mid + 1, end)
                merge(arr, start, mid, end)

        merge_sort_alg(self.arr, 0, self.n - 1)
        return frames

    def quick_sort(self):
        frames = []
        def partition(arr, low, high):
            pivot = arr[(low + high) // 2]
            i, j = low, high
            swapped = set()
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swapped.add(i)
                    swapped.add(j)
                    i += 1
                    j -= 1
                    frames.append((arr.copy(), swapped))
            return i

        def quick_sort_alg(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_alg(arr, low, pi - 1)
                quick_sort_alg(arr, pi, high)

        quick_sort_alg(self.arr, 0, self.n - 1)
        return frames

    def heap_sort(self):
        frames = []
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            swapped = set()
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                swapped.add(i)
                swapped.add(largest)
                frames.append((arr.copy(), swapped))
                heapify(arr, n, largest)

        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(self.arr, n, i)
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            swapped = {i, 0}
            frames.append((self.arr.copy(), swapped))
            heapify(self.arr, i, 0)
        return frames

    def start(self, alg_name):
        self.reset_array()
        self.alg_name = alg_name
        frames = self.algs[alg_name]()
        self.animate(frames)

    def save(self, filename):
        self.anim.save(filename, writer='imagemagick')

    def __repr__(self):
        return f'{self.alg_name} Sort'

def main():
    arr = [random.randint(1, 50) for _ in range(20)]
    hl = True
    sort = Sort(arr, highlight=hl)
    for alg_name in sort.algs:
        sort.start(alg_name)
        sort.save(f'{alg_name.lower().replace(" ", "_")}_{hl}.gif')

if __name__ == '__main__':
    main()
