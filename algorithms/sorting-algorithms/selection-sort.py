# Author : Jay Gohil

a = [1,23,45,89,24,56]
print(a)

def selection_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            iterations += 1
            if array[minimum_index] > array[j]:
                minimum_index = j
        
        # Swap the found minimum element with 
        # the first element
        if minimum_index != i:
            array[i], array[minimum_index] = array[minimum_index], array[i]

selection_sort(a)
print(a)
