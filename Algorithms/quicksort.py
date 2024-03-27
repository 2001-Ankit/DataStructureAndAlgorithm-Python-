def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp



def partition(elements,start,end):
    pivot_index = 0
    pivot = elements[pivot_index]
    while start < end:
        while elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,elements)

    swap(pivot_index,end,elements)

    return end



def quick_sort(elements,start,end):
    partition(elements,start,end)



if __name__=='__main':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements,0,len(elements)-1)
    print(elements)
