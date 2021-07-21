class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head):
        self.head = head
    # Get data of element at given index
    # O(n)
    def read(self, index):
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next_node
            current_index += 1

            if not current:
                return None
        return current.data

    # Get index of given value
    # O(n)
    def index(self, value):
        current = self.head
        current_index = 0
        while current:
            # Value is found
            if current.value == value:
                return current_index

            current = current.next_node
            current_index += 1

        # Value is not in list
        return None

    # O(n)
    def append(self, value):
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(value)

    # O(n), O(1) at beginning
    def insert(self, index, value):
        current = self.head
        current_index = 0
        while current:
            if current_index == index - 1:
                new_node = Node(value)
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node
            current_index += 1
        raise IndexError("Index is out of range")

    # O(n)
    def print_list(self):
        current = self.head
        while current.next_node:
            print (f"{current.value} -> ", end="")
            current = current.next_node
        print (current.value)

    # O(n), O(1) at beginning
    def delete_value(self, value):
        current = self.head
        while current.next_node:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node
        raise ValueError("The value is not in the list")

    # O(n), O(1) at beginning
    def delete_index(self, index):
        current = self.head
        current_index = 0
        while current.next_node:
            if current_index + 1 == index:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node
            current_index += 1
        raise IndexError("Index is out of range")
