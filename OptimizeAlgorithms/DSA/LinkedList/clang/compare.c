#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Định nghĩa cấu trúc Node cho LinkedList
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Định nghĩa LinkedList
typedef struct LinkedList {
    Node* head;
    Node* tail;
} LinkedList;

// Hàm khởi tạo Node mới
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Hàm khởi tạo LinkedList
LinkedList* createLinkedList() {
    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    if (list == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    list->head = NULL;
    list->tail = NULL;
    return list;
}

// Hàm thêm Node vào cuối LinkedList
void addToTail(LinkedList* list, int data) {
    Node* newNode = createNode(data);
    if (list->head == NULL) {
        list->head = newNode;
        list->tail = newNode;
    } else {
        list->tail->next = newNode;
        list->tail = newNode;
    }
}

// Hàm cập nhật Node trong LinkedList
void setNode(LinkedList* list, int index, int data) {
    Node* current = list->head;
    int currentIndex = 0;
    while (current != NULL && currentIndex < index) {
        current = current->next;
        currentIndex++;
    }
    if (current != NULL) {
        current->data = data;
    }
}

// Hàm xóa Node khỏi LinkedList
void removeNode(LinkedList* list, int data) {
    Node* temp = list->head;
    Node* prev = NULL;
    
    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) {
        return; // Không tìm thấy Node cần xóa
    }
    
    if (prev == NULL) {
        // Xóa Node đầu danh sách
        list->head = temp->next;
    } else {
        prev->next = temp->next;
    }
    
    if (temp == list->tail) {
        list->tail = prev;
    }
    
    free(temp);
}

// Định nghĩa cấu trúc ArrayList
typedef struct ArrayList {
    int* array;
    int capacity;
    int size;
} ArrayList;

// Hàm khởi tạo ArrayList
ArrayList* createArrayList(int capacity) {
    ArrayList* list = (ArrayList*)malloc(sizeof(ArrayList));
    if (list == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    list->array = (int*)malloc(capacity * sizeof(int));
    if (list->array == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    list->capacity = capacity;
    list->size = 0;
    return list;
}

// Hàm thêm phần tử vào cuối ArrayList
void add(ArrayList* list, int data) {
    if (list->size < list->capacity) {
        list->array[list->size] = data;
        list->size++;
    } else {
        // Xử lý khi mảng đầy
        printf("ArrayList is full.\n");
    }
}

// Hàm cập nhật phần tử trong ArrayList
void set(ArrayList* list, int index, int data) {
    if (index >= 0 && index < list->size) {
        list->array[index] = data;
    } else {
        printf("Index out of bounds.\n");
    }
}

// Hàm xóa phần tử khỏi ArrayList
void removeAtIndex(ArrayList* list, int index) {
    if (index >= 0 && index < list->size) {
        for (int i = index; i < list->size - 1; i++) {
            list->array[i] = list->array[i + 1];
        }
        list->size--;
    } else {
        printf("Index out of bounds.\n");
    }
}

// Hàm so sánh thời gian chạy
void timeComparison() {
    int n = 20000;
    
    // Đo thời gian chạy cho LinkedList
    LinkedList* linkedList = createLinkedList();
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        addToTail(linkedList, i);
    }
    clock_t end = clock();
    double linkedListAddTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    start = clock();
    for (int i = 0; i < n; i++) {
        setNode(linkedList, i, i * 2);
    }
    end = clock();
    double linkedListSetTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    start = clock();
    for (int i = 0; i < n; i++) {
        removeNode(linkedList, i);
    }
    end = clock();
    double linkedListRemoveTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    // Đo thời gian chạy cho ArrayList
    ArrayList* arrayList = createArrayList(n);
    start = clock();
    for (int i = 0; i < n; i++) {
        add(arrayList, i);
    }
    end = clock();
    double arrayListAddTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    start = clock();
    for (int i = 0; i < n; i++) {
        set(arrayList, i, i * 2);
    }
    end = clock();
    double arrayListSetTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    start = clock();
    for (int i = 0; i < n; i++) {
        removeAtIndex(arrayList, i);
    }
    end = clock();
    double arrayListRemoveTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    // In ra kết quả so sánh
    printf("Linked List - Add Time: %.6f seconds\n", linkedListAddTime);
    printf("Linked List - Set Time: %.6f seconds\n", linkedListSetTime);
    printf("Linked List - Remove Time: %.6f seconds\n", linkedListRemoveTime);
    printf("Array List - Add Time: %.6f seconds\n", arrayListAddTime);
    printf("Array List - Set Time: %.6f seconds\n", arrayListSetTime);
    printf("Array List - Remove Time: %.6f seconds\n", arrayListRemoveTime);
    
    // Giải phóng bộ nhớ
    free(linkedList);
    free(arrayList->array);
    free(arrayList);
}

int main() {
    timeComparison();
    return 0;
}
