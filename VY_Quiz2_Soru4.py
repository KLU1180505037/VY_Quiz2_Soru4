
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Kuyruk boş!")
            return
        temp_node = self.front
        self.front = temp_node.next
        if self.front is None:
            self.rear = None

    def display(self):
        if self.is_empty():
            print("Kuyruk boş!")
            return
        temp_node = self.front
        while temp_node is not None:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next

queue = Queue()

while True:
    print("\nKuyruk işlemleri için seçenekler:\n1. Eleman Ekle\n2. Eleman Çıkar\n3. Kuyruğu Görüntüle\n4. Çıkış")
    choice = int(input("Seçeneği girin: "))
    if choice == 1:
        data = input("Eklenecek elemanı girin: ")
        queue.enqueue(data)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Geçersiz seçenek!")
