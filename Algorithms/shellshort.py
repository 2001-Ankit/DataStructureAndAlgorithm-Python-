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
    tests=[[11,9,29,7,2,15,28],[3,7,9,11],[25,22,21,10],[29,15,28],[],[6]]
    for test in tests:
        arr = test
        print("Array before sorting: ", arr)
        shellsort(arr)
        print("Array after sorting: ", arr)


    arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print("Array before sorting: ", arr)
    shellsort(arr)
    print("Array after sorting: ", arr)

