class heap:
    def __init__(self):
        self.data = []

    @property
    def first(self):
        if self.data:
            return self.data[0]
        return None

    @property
    def last(self):
        if self.data:
            return self.data[-1]
        return None

    def left_index(self, index):
        return (index * 2) + 1

    def right_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    # O(log n)
    def insert(self, value):
        # Add value to end
        self.data.append(value)

        # Set index to be last index in heap
        new_index = len(self.data) - 1

        while new_index > 0 and self.data[new_index] > self.data[self.parent_index(new_index)]:
            #Swap node with parent and update index
            self.data[new_index], self.data[self.parent_index(new_index)] = self.data[self.parent_index(new_index)], self.data[new_index]
            new_index = self.parent_index(new_index)

    # O(log n)
    # Only ever delete root node
    def delete(self):
        # Move last node to top
        self.data[0] = self.data.pop()

        node_index = 0

        while self.greater_child(node_index):
            larger_child_index = self.get_larger_child_index(node_index)

            # Swap trickle node with larger child
            self.data[node_index], self.data[larger_child_index] =  self.data[larger_child_index], self.data[node_index]
            node_index = larger_child_index

    def greater_child(self, index):
        """ Check if node at given index has left or right children
        and if either of the children are greater than the node at the index"""
        left_index = self.left_index(index)
        right_index = self.right_index(index)
        try:
            condition_one = self.data[left_index] and self.data[left_index] > self.data[index]
        except IndexError:
            condition_one = False

        try:
            condition_two = self.data[right_index] and self.data[right_index] > self.data[index]
        except IndexError:
            condition_two = False
        return condition_one or condition_two

    def get_larger_child_index(self, index):
        left_index = self.left_index(index)
        right_index = self.right_index(index)

        # If there is no right child
        try:
            if not self.data[right_index]:
                return left_index
        except IndexError:
            return left_index

        # If right child is greater than left child
        if self.data[right_index] > self.data[left_index]:
            return right_index
        else:
            return left_index

    def __str__(self):
        return f"{self.data}"


a = heap()
for i in range(10):
    a.insert(i)

print (a)
a.delete()
print (a)
