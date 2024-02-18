class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Heap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()
    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop()
        self.heapify_down()
        return min_value
    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
    def heapify_down(self):
        index = 0
        while index < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index >= len(self.heap):
                break
            if right_child_index >= len(self.heap):
                min_child_index = left_child_index
            else:
                if self.heap[left_child_index] < self.heap[right_child_index]:
                    min_child_index = left_child_index
                else:
                    min_child_index = right_child_index
            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BalancedTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class TSPSolver():
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.visited[0] = True
        self.min_cost = float('inf')
        self.path = [] 

    def tsp(self, node, cost, count, current_path):
        if count == len(self.graph) and self.graph[node][0] > 0:
            self.min_cost = min(self.min_cost, cost + self.graph[node][0])
            self.path = current_path + [node]  
            return
        for i in range(len(self.graph)):
            if not self.visited[i] and self.graph[node][i] > 0:
                self.visited[i] = True
                self.tsp(i, cost + self.graph[node][i], count + 1, current_path + [node])
                self.visited[i] = False

    def solve(self):
        self.tsp(0, 0, 1, [])
        return self.min_cost
    
    def print_path(self):
        return ' -> '.join(map(str, self.path))
    
class GreedySolver():
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.visited[0] = True
        self.min_cost = 0
        self.path = []

    def get_next_node(self, current):
        min_cost = float('inf')
        next_node = 0
        for i in range(len(self.graph)):
            if not self.visited[i] and self.graph[current][i] > 0:
                if self.graph[current][i] < min_cost:
                    min_cost = self.graph[current][i]
                    next_node = i
        return next_node
    
    def solve(self):
        current = 0
        for _ in range(len(self.graph) - 1):
            next_node = self.get_next_node(current)
            self.visited[next_node] = True
            self.min_cost += self.graph[current][next_node]
            self.path.append(current)
            current = next_node
        self.min_cost += self.graph[current][0]
        self.path.append(current)
        return self.min_cost
    
    def print_path(self):
        return ' -> '.join(map(str, self.path))

class DynamicSolver():
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.visited[0] = True
        self.min_cost = float('inf')
        self.dp = [[-1] * (1 << len(graph)) for _ in range(len(graph))]
        
    def tsp(self, node, mask):
        if mask == (1 << len(self.graph)) - 1:
            return self.graph[node][0]
        if self.dp[node][mask] != -1:
            return self.dp[node][mask]
        min_cost = float('inf')
        for i in range(len(self.graph)):
            if not (mask & (1 << i)) and self.graph[node][i] > 0:
                min_cost = min(min_cost, self.graph[node][i] + self.tsp(i, mask | (1 << i)))
        self.dp[node][mask] = min_cost
        return min_cost
    def solve(self):
        return self.tsp(0, 1)

class BubbleSort:
    def sort(self, nums, print_animation=False):
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    if print_animation:
                        self._print_animation(nums, i, j)
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    
    def _print_animation(self, nums, i, j):
        print(f'Iteration: {i + 1}, Index: {j + 1}, Array: {nums}')
 
class SelectionSort:
    def sort(self, nums, print_animation=False):
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if i != min_index:
                if print_animation:
                    self._print_animation(nums, i, min_index)
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
    
    def _print_animation(self, nums, i, min_index):
        print(f'Iteration: {i + 1}, Min Index: {min_index + 1}, Array: {nums}')

class InsertionSort:
    def sort(self, nums, print_animation=False):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
            if print_animation:
                self._print_animation(nums, i, j)
        return nums
    
    def _print_animation(self, nums, i, j):
        print(f'Iteration: {i + 1}, Key: {nums[i]}, Array: {nums}')

class MergeSort:
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def sort(self, nums, print_animation=False):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])
        if print_animation:
            self._print_animation(left, right)
        return self.merge(left, right)
    
    def _print_animation(self, left, right):
        print(f'Left: {left}, Right: {right}')

class QuickSort:
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
    def sort(self, nums, low, high, print_animation=False):
        if low < high:
            pi = self.partition(nums, low, high)
            if print_animation:
                self._print_animation(nums, pi)
            self.sort(nums, low, pi - 1)
            self.sort(nums, pi + 1, high)
        return nums
    
    def _print_animation(self, nums, pi):
        print(f'Pivot: {nums[pi]}, Array: {nums}')

class HeapSort:
    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[i] < nums[left]:
            largest = left
        if right < n and nums[largest] < nums[right]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)
    
    def sort(self, nums, print_animation=False):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
            if print_animation:
                self._print_animation(nums, i)
        return nums
    
    def _print_animation(self, nums, i):
        print(f'Iteration: {i + 1}, Array: {nums}')

class CountingSort:
    def sort(self, nums, print_animation=False):
        max_num = max(nums)
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        result = [0] * len(nums)
        for num in nums:
            result[count[num] - 1] = num
            count[num] -= 1
        if print_animation:
            self._print_animation(result)
        return result
    
    def _print_animation(self, result):
        print(f'Array: {result}')

class RadixSort:
    def sort(self, nums, print_animation=False):
        max_num = max(nums)
        exp = 1
        while max_num // exp > 0:
            self.count_sort(nums, exp, print_animation)
            exp *= 10
        return nums
    
    def count_sort(self, nums, exp, print_animation):
        n = len(nums)
        count = [0] * 10
        result = [0] * n
        for num in nums:
            count[(num // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            result[count[(nums[i] // exp) % 10] - 1] = nums[i]
            count[(nums[i] // exp) % 10] -= 1
        for i in range(n):
            nums[i] = result[i]
        if print_animation:
            self._print_animation(nums)
    
    def _print_animation(self, nums):
        print(f'Array: {nums}')

class BucketSort:
    def sort(self, nums, print_animation=False):
        max_num = max(nums)
        min_num = min(nums)
        bucket_size = 10
        bucket_count = (max_num - min_num) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        for num in nums:
            index = (num - min_num) // bucket_size
            buckets[index].append(num)
        for i in range(bucket_count):
            buckets[i] = sorted(buckets[i])
        result = []
        for bucket in buckets:
            result.extend(bucket)
        if print_animation:
            self._print_animation(result)
        return result
    
    def _print_animation(self, result):
        print(f'Array: {result}')

class ShellSort:
    def sort(self, nums, print_animation=False):
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
                if print_animation:
                    self._print_animation(nums, gap, i, j)
            gap //= 2
        return nums
    
    def _print_animation(self, nums, gap, i, j):
        print(f'Gap: {gap}, Iteration: {i + 1}, Index: {j + 1}, Array: {nums}')

class CocktailSort:
    def sort(self, nums, print_animation=False):
        n = len(nums)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if nums[i] > nums[i + 1]:
                    if print_animation:
                        self._print_animation(nums, i)
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if nums[i] > nums[i + 1]:
                    if print_animation:
                        self._print_animation(nums, i)
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
            start += 1
        return nums
    
    def _print_animation(self, nums, i):
        print(f'Index: {i + 1}, Array: {nums}')

class BinarySearch:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

class LinearSearch:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

class JumpSearch:
    def search(self, nums, target):
        n = len(nums)
        step = int(n ** 0.5)
        prev = 0
        while nums[min(step, n) - 1] < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while nums[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1
        if nums[prev] == target:
            return prev
        return -1

class InterpolationSearch:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high and target >= nums[low] and target <= nums[high]:
            mid = low + (high - low) * (target - nums[low]) // (nums[high] - nums[low])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
class ExponentialsSearch:
    def search(self, nums, target):
        n = len(nums)
        if nums[0] == target:
            return 0
        i = 1
        while i < n and nums[i] <= target:
            i *= 2
        return self.binary_search(nums, i // 2, min(i, n), target)
    

    def binary_search(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1