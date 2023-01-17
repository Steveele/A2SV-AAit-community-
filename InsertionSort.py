def insertionSort1(n, arr):
    current = arr[-1]
    i = n - 1
    while i > 0 and arr[i-1] > current:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = current
    print(*arr)
