"""
Uses 0-based indexing.

Doesn't use OOP, that is, classes. It's in procedural paradigm.

Also includes functions for Partial Sorting.
"""

def parent(i):
    return (i - 1)//2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def siftDownMax(H, i, size):
    """Sifts the element with index i down until it finds its place.
       Taken from MaxHeap class.
       O(log n)
    """
    while i < size:
        maxIndex = i
        l = leftChild(i)
        if l < size and H[l] > H[maxIndex]:
            maxIndex = l
        r = rightChild(i)
        if r < size and H[r] > H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            H[i], H[maxIndex] = H[maxIndex], H[i]
            i = maxIndex
        else:
            break

def siftDownMin(H, i, size):
    """Sifts the element with index i down until it finds its place.
       Taken from MinHeap class.
       O(log n)
    """
    while i < size:
        maxIndex = i
        l = leftChild(i)
        if l < size and H[l] < H[maxIndex]:
            maxIndex = l
        r = rightChild(i)
        if r < size and H[r] < H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            H[i], H[maxIndex] = H[maxIndex], H[i]
            i = maxIndex
        else:
            break

def extractMax(H, size):
    """Returns the element with the highest value (priority).
       Taken from MaxHeap class.
       O(log n)"""
    if size >= 1:
        result = H[0]
        H[0] = H[size-1]
        size -= 1
        siftDownMax(H, 0, size)
        return result
    else:
        raise Exception("The heap is empty! Cannot return the element with the highest value.")

def extractMin(H, size):
    """Returns the element with the lowest value (priority).
       Taken from MinHeap class.
       O(log n)"""
    if size >= 1:
        result = H[0]
        H[0] = H[size-1]
        size -= 1
        siftDownMin(H, 0, size)
        return result
    else:
        raise Exception("The heap is empty! Cannot return the element with the lowest value.")

def buildHeapMax(A, n):
    """Turns the given array A with length n into a heap. Works in-place.
       Inputs: A, n
       Its time complexity is actually O(2n), which is O(n), and it doesn't use additional space.
    """
    size = n       # n = len(A)
    for i in range(n//2, -1, -1):
        siftDownMax(A, i, size)

def buildHeapMin(A, n):
    """Turns the given array A with length n into a heap. Works in-place.
       Inputs: A, n
       Its time complexity is actually O(2n), which is O(n), and it doesn't use additional space.
    """
    size = n       # n = len(A)
    for i in range(n//2, -1, -1):
        siftDownMin(A, i, size)

def heapSortNonDescending(A, n):
    """Turns the given array A with length n into a heap, and then it sorts it in-place.
       It doesn't return A, because it sorts it in-place.
       Its time complexity is O(n log n), and it doesn't use additional space.
    """
    buildHeapMax(A, n)
    size = n
    for _ in range(n):
        A[0], A[size-1] = A[size-1], A[0]
        size -= 1
        siftDownMax(A, 0, size)

def heapSortNonAscending(A, n):
    """Turns the given array A with length n into a heap, and then it sorts it in-place.
       It doesn't return A, because it sorts it in-place.
       Its time complexity is O(n log n), and it doesn't use additional space.
    """
    buildHeapMin(A, n)
    size = n
    for _ in range(n):
        A[0], A[size-1] = A[size-1], A[0]
        size -= 1
        siftDownMin(A, 0, size)

def partialSortingMax(A, n, k):
    """Inputs: Array A[1, n]; n, which is len(A); Integer k, such that 1 <= k <= n
       Output: The last (maximal) k elements of a sorted version of A.
       O(n), if k <= O(n/log n)
    """
    assert 1 <= k <= n
    A = A[:]        # This works! This is if we want to preserve the input array A - otherwise, it gets destroyed.
    buildHeapMax(A, n)
    result = []
    for i in range(k):
        result.append(extractMax(A, n-i))
    return result

def partialSortingMin(A, n, k):
    """Inputs: Array A[1, n]; n, which is len(A); Integer k, such that 1 <= k <= n
       Output: The last (minimal) k elements of a sorted version of A.
       O(n), if k <= O(n/log n)
    """
    assert 1 <= k <= n
    A = A[:]        # This works! This is if we want to preserve the input array A - otherwise, it gets destroyed.
    buildHeapMin(A, n)
    result = []
    for i in range(k):
        result.append(extractMin(A, n-i))
    return result



if __name__ == "__main__":
    elts = [11, 13, 12, 18, 14, 42, 7, 18, 29]              # len(elts) = 9
    n = len(elts)
    k = n                                                   # Test with boundary cases, especially with k = n.

    A = elts[:]
    heapSortNonDescending(A, n)                             # Sorts the array in place! A will be sorted after this!
    print(A, elts)
    print()

    #A = elts[:]
    heapSortNonAscending(A, n)                              # Sorts the array in place! A will be sorted after this!
    print(A, elts)
    print()

    #A = elts[:]
    print(partialSortingMax(A, n, k))
    print(A, elts)
    print()

    #A = elts[:]
    print(partialSortingMin(A, n, k))
    print(A, elts)
    print()
