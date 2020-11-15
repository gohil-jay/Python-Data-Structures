#Author: Jay Gohil

a = [1,45,23,67,29]
print(a)

def bubble_sort(array):
    n=len(array)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] # swap


bubble_sort(a)
print(a)

#-------------------------------------------------------------------------

def optimized_bubble_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1):
            iterations += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # if no swapping is performed that means sorting is complete
        # hence break out of the loop
        if not swapped:          
            break
