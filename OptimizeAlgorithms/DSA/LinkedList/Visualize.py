# Định nghĩa lớp Node cho danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Định nghĩa lớp LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Thêm phần tử vào đầu danh sách liên kết
    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Tìm phần tử cuối cùng và thêm vào cuối danh sách liên kết
    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        
        # Trường hợp đặc biệt: chèn vào đầu danh sách
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        current_position = 0
        
        # Tìm node ở vị trí trước vị trí cần chèn
        while current_position < position - 1 and current.next:
            current = current.next
            current_position += 1
        
        # Nếu position lớn hơn số lượng node hiện tại, chèn vào cuối danh sách
        if current is None:
            print("Position is out of bounds.")
            return
        
        # Chèn node mới vào sau node hiện tại
        new_node.next = current.next
        current.next = new_node
    
    def set(self, key, data):
        temp = self.head
        while temp:
            if temp.data == key:
                temp.data = data
                return
            temp = temp.next

    # Xóa phần tử khỏi danh sách liên kết
    def remove(self, key):
        temp = self.head
        if temp:
            if temp.data == key:
                self.head = temp.next
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
        temp = None
    
    # Hiển thị danh sách liên kết
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")

# Định nghĩa lớp ArrayList
class ArrayList:
    def __init__(self):
        self.array = []
    
    # Thêm phần tử vào mảng
    def add(self, data):
        self.array.append(data)
    
    # Sửa phần tử trong mảng tại vị trí index
    def set(self, index, data):
        if index < len(self.array):
            self.array[index] = data
    
    def insert(self, index, data):
        if index < len(self.array):
            self.array.insert(index, data)
    
    # Xóa phần tử trong mảng tại vị trí index
    def remove(self, index):
        if index < len(self.array):
            self.array.pop(index)
    
    # Hiển thị mảng
    def display(self):
        print(self.array)

# Minh họa sử dụng
if __name__ == "__main__":
    # Sử dụng LinkedList
    print("Linked List:")
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_tail(3)
    linked_list.display()
    linked_list.add_to_head(0)
    linked_list.display()
    linked_list.insert_after(linked_list.head.next, 1.5)
    linked_list.display()
    linked_list.insert_at_position(2, 1.25)
    linked_list.display()
    linked_list.set(1, 1.75)
    linked_list.display()
    linked_list.remove(2)
    linked_list.display()
    
    # Sử dụng ArrayList
    print("\nArray:")
    array_list = ArrayList()
    array_list.add(1)
    array_list.add(2)
    array_list.add(3)
    array_list.display()
    array_list.set(1, 1.5)
    array_list.display()
    array_list.insert(1, 1.25)
    array_list.display()
    array_list.remove(2)
    array_list.display()
    
    def time_comparison():
        import time
        linked_list = LinkedList()
        array_list = ArrayList()
        n = 10000
        start = time.time()
        for i in range(n):
            linked_list.add_to_tail(i)
        end = time.time()
        print(f"Linked List: {end - start}")
        start = time.time()
        for i in range(n):
            array_list.add(i)
        end = time.time()
        print(f"Array List: {end - start}")

    time_comparison()