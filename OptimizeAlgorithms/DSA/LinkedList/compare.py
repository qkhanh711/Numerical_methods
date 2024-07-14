import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
    
    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def insert_at_position(self, position, data):
        if position == 0:
            self.add_to_head(data)
            return
        
        new_node = Node(data)
        current = self.head
        current_position = 0
        
        while current_position < position - 1 and current:
            current = current.next
            current_position += 1
        
        if not current:
            print("Position is out of bounds.")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def set(self, key, data):
        temp = self.head
        while temp:
            if temp.data == key:
                temp.data = data
                return
            temp = temp.next
    
    def remove(self, key):
        temp = self.head
        
        if temp and temp.data == key:
            self.head = temp.next
            if not self.head:
                self.tail = None
            temp = None
            return
        
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if not temp:
            return
        
        prev.next = temp.next
        
        if temp == self.tail:
            self.tail = prev
        
        temp = None
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

class ArrayList:
    def __init__(self):
        self.array = []
    
    def add(self, data):
        self.array.append(data)
    
    def set(self, index, data):
        if index < len(self.array):
            self.array[index] = data
    
    def remove(self, index):
        if index < len(self.array):
            self.array.pop(index)
    
    def display(self):
        print(self.array)

def time_comparison():
    n = 10000
    
    # Thời gian chạy LinkedList
    linked_list = LinkedList()
    start = time.time()
    for i in range(n):
        linked_list.add_to_tail(i)
    end = time.time()
    linked_list_add_time = end - start
    
    start = time.time()
    for i in range(n):
        linked_list.set(i, i*2)
    end = time.time()
    linked_list_set_time = end - start
    
    start = time.time()
    for i in range(n):
        linked_list.remove(i)
    end = time.time()
    linked_list_remove_time = end - start
    
    # Thời gian chạy ArrayList
    array_list = ArrayList()
    start = time.time()
    for i in range(n):
        array_list.add(i)
    end = time.time()
    array_list_add_time = end - start
    
    start = time.time()
    for i in range(n):
        array_list.set(i, i*2)
    end = time.time()
    array_list_set_time = end - start
    
    start = time.time()
    for i in range(n):
        array_list.remove(i)
    end = time.time()
    array_list_remove_time = end - start
    
    # In ra kết quả so sánh
    print(f"Linked List - Add Time: {linked_list_add_time}")
    print(f"Linked List - Set Time: {linked_list_set_time}")
    print(f"Linked List - Remove Time: {linked_list_remove_time}")
    print(f"Array List - Add Time: {array_list_add_time}")
    print(f"Array List - Set Time: {array_list_set_time}")
    print(f"Array List - Remove Time: {array_list_remove_time}")

if __name__ == "__main__":
    time_comparison()
