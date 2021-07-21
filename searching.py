# O(n)
def linear_search(arr, item):
    for n, i in enumerate(arr):
        if i == item:
            #Item found
            return n
    #Item not found
    return None

# O(log n)
def binary_search(arr, item):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        #Get middle item
        mid = (lower + upper) // 2

        if arr[mid] == item:
            #If you have the item being searched for
            return mid
        elif item < arr[mid]:
            #Item lower than mid
            upper = mid - 1
        else:
            #Item higher than mid
            lower = mid + 1
    #Item not found
    return None

print (binary_search([1, 2, 3, 4, 5], 6))
