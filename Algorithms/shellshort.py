def shellsort(arr):
    size = len(arr)
    gap = size//2
    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j>=gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
            gap = gap//2


if __name__ == '__main__':
    tests=[[11,9,29,7,2,2,15,11,28],[3,7,9,11],[25,22,21,10],[29,15,28],[],[6]]
    for test in tests:
        arr = test
        print("Array before sorting: ", arr)
        shellsort(arr)
        print("Array after sorting: ", arr)

    arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print("Array before sorting: ", arr)
    shellsort(arr)
    print("Array after sorting: ", arr)



def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div
elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9,  5, 8, 3]

print(f'Given unsorted list: {elements}')
shell_sort(elements)
print(f'List after Sorting : {elements}')
