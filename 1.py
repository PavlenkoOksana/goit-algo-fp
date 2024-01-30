class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  # реверсування однозв'язного списку
  def revers_list(self):
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  # алгоритм сортування вставками для однозв'язного списку;
  def insertion_sort_list(self):
    if self.head is None or self.head.next is None:
            return  # Немає чого сортувати, якщо список пустий або містить лише один елемент

    sorted_head = None 
    current = self.head

    while current:
            next_node = current.next  
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node  
    self.head = sorted_head  

# функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge_sorted_lists(list1, list2):
    # Створюємо новий пустий відсортований список
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    # Проходимо обидва списки, порівнюючи значення вузлів
    while current1 is not None and current2 is not None:
        if current1.data < current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

    # Додавання залишкових елементів, якщо один зі списків закінчився раніше
    while current1 is not None:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next

    while current2 is not None:
        merged_list.insert_at_end(current2.data)
        current2 = current2.next

    return merged_list

if __name__ == "__main__":
  llist_1 = LinkedList()
  llist_2 = LinkedList()

  # Вставляємо вузли в початок
  llist_1.insert_at_beginning(5)
  llist_1.insert_at_beginning(10)
  llist_1.insert_at_beginning(15)

  # Вставляємо вузли в кінець
  llist_1.insert_at_end(20)
  llist_1.insert_at_end(25)

  llist_2.insert_at_beginning(45)
  llist_2.insert_at_beginning(50)
  llist_2.insert_at_beginning(40)

  print("Оригінальний список №1:")
  llist_1.print_list()

  llist_1.revers_list()
  print("\nЗворотній список №1:")
  llist_1.print_list()

  llist_1.insertion_sort_list()
  print("\nВідсортований список №1:")
  llist_1.print_list()

  print("\nОригінальний список №2:")
  llist_2.print_list()

  llist_2.insertion_sort_list()
  print("\nВідсортований список №2:")
  llist_2.print_list()

  merged_list = merge_sorted_lists(llist_1, llist_2)
  print("\nОб'єднаний список:")
  merged_list.print_list()



