def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        a = arr[b]
        b = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)

    return end

def quick_sort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index-1)
        quick_sort(elements, partition_index+1, end)



if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)