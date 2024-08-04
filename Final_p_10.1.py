# Визначення класу вузла однозв'язного списку
class Node:
    def __init__(self, data=None):
        self.data = data  # Дані вузла
        self.next = None  # Посилання на наступний вузол

# Визначення класу однозв'язного списку
class LinkedList:
    def __init__(self):
        self.head = None  # Початкове посилання на голову списку

    # Метод для додавання нового вузла в кінець списку
    def append(self, data):
        new_node = Node(data)  # Створення нового вузла
        if self.head is None:
            self.head = new_node  # Якщо список порожній, новий вузол стає головою
            return
        last = self.head
        while last.next:
            last = last.next  # Пошук останнього вузла в списку
        last.next = new_node  # Додавання нового вузла в кінець списку

    # Метод для виведення елементів списку
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Функція для реверсування однозв'язного списку
def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current is not None:
        next_node = current.next
        current.next = prev  # Зміна посилання на попередній вузол
        prev = current
        current = next_node
    linked_list.head = prev  # Оновлення голови списку

# Функція для вставки вузла у відсортований список
def sorted_insert(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node
    current = sorted_head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_head

# Функція для сортування однозв'язного списку методом вставок
def insertion_sort(linked_list):
    sorted_head = None
    current = linked_list.head
    while current is not None:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    linked_list.head = sorted_head

# Функція для об'єднання двох відсортованих однозв'язних списків
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклад використання

# Створення та заповнення першого списку
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
print("Перший список:")
list1.print_list()

# Створення та заповнення другого списку
list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
print("Другий список:")
list2.print_list()

# Реверсування першого списку
reverse_list(list1)
print("Реверсований перший список:")
list1.print_list()

# Сортування першого списку вставками
insertion_sort(list1)
print("Відсортований перший список:")
list1.print_list()

# Об'єднання двох відсортованих списків
merged_list = merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
