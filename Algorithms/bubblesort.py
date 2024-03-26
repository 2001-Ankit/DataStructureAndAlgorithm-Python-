def bubble_sort(elements):
    size = len(elements)
    swapped = False
    for i in range(size-1):
        for j in range(size-1):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break
if __name__ == '__main__':
    elements = [45,12,40,8,15,25]
    bubble_sort(elements)
    print(elements)