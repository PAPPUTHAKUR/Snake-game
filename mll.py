class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def printing_ll(self):
        if self.head == None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            else:
                n = n.next  

        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head

        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linklist is  not empty")

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.next

    def delete_atend(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None


ll1 = Linked_list()
ll1.add_begin(10)
ll1.add_begin(50)
ll1.add_end(67)
ll1.add_end(68)
ll1.add_before(118, 50)
ll1.add_after(78, 67)
ll1.delete_begin()

ll1.printing_ll()
