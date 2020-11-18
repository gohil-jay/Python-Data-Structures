#Author: Jay Gohil

a = [1,29,34,12,56,34,89,45]
print(a)

def partition(array, low, high):
    i = low - 1            # index of smaller element
    pivot = array[high]    # pivot 
    
    for j in range(low, high):
        # If current element is smaller than the pivot
        
        if array[j] < pivot:
        # increment index of smaller element
        
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place 
        temp = partition(array, low, high)
        
        # Separately sort elements before
        # partition and after partition 
        quick_sort(array, low, temp - 1)
        quick_sort(array, temp + 1, high)

quick_sort(a, 0, (len(a)-1))
print(a)
