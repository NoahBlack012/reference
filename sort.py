# O(n^2)
def bubble_sort(arr):
    unsorted_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index):
            #If item below in list is larger than above item in list
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False

        unsorted_index -= 1
    return arr

# O((n^2) / 2)
def selection_sort(arr):
    for n, i in enumerate(arr):
        lowest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        if lowest_index != i:
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
    return arr

"""
Best Case: O(n)
Average/Worst Case O(n^2)
"""
def insertion_sort(arr):
    #Go through each value execpt the 1st value
    for index in range(1, len(arr)):
        # Get temp value at index, position in index one below
        temp = arr[index]
        pos = index - 1

        """Go through each value below position until
        you find a value smaller than the temp value"""
        while pos >= 0:
            # Shift value up if it is greater than temp
            if arr[pos] > temp:
                arr[pos+1] = arr[pos]
                pos -= 1
            else:
                break
        arr[pos+1] = temp
    return arr

""" Quicksort:
Best/Average Case: O(n log n)
Worst Case: O(n^2)
"""
class sortable_arr:
    def __init__(self, arr):
        self.arr = arr

    # O(n)
    def partition(self, left_pointer, right_pointer):
        #Pivot is furthest right element
        pivot_index = right_pointer
        pivot = self.arr[pivot_index]

        #Right pointer is one left of the pivot
        right_pointer -= 1

        #Loop until left and right pointers meet
        while True:
            """Move left pointer right until it points
            to a value larger than the pivot"""
            while self.arr[left_pointer] < pivot:
                left_pointer += 1

            """Move right pointer left until it points
            to a value smaller than the pivot"""
            while self.arr[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                #If the pointers have not met, swap the values
                self.arr[left_pointer], self.arr[right_pointer] = self.arr[right_pointer], self.arr[left_pointer]
                left_pointer += 1

        self.arr[left_pointer], self.arr[pivot_index] = self.arr[pivot_index], self.arr[left_pointer]
        return left_pointer

    # O(n log n) --> O(n^2)
    def quicksort(self, left_index, right_index):
        #Base case: If subarray has 0 or 1 elements
        if right_index - left_index <= 0:
            return

        #Partition range of elements
        pivot_index = self.partition(left_index, right_index)

        #Recursively call quicksort on elements left of the pivot
        self.quicksort(left_index, pivot_index - 1)

        #Recursively call quicksort on elements right of the pivot
        self.quicksort(pivot_index + 1, right_index)

    # O(n)
    def quickselect(self, nth_lowest_value, left_index, right_index):
        #Base Case: Array has one cell, item found
        if right_index - left_index <= 0:
            return self.arr[left_index]

        pivot_index = self.partition(left_index, right_index)

        if nth_lowest_value < pivot_index:
            return self.quickselect(nth_lowest_value, left_index, pivot_index - 1)
        elif nth_lowest_value > pivot_index:
            return self.quickselect(nth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.arr[pivot_index]
