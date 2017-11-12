# Testing the Heaps module.

import Heaps

def testMaxPriorityQueue(elts, maxSize):
    
    pq = Heaps.MaxPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        print("Max element: {}".format(pq.extractMax()))
    except Exception as e:
        print(e)
    try:
        pq.remove(0)
    except Exception as e:
        print(e)
    try:
        pq.remove(1)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(100)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    print("Max element: {}".format(pq.extractMax()))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(123)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(1)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    size = len(elts)
    for i in range(size):
        pq.insert(elts[i])
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    pq.insert(17)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    pq.insert(17)
    try:
        pq.insert(123)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.insert(50)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.remove(pq.getPriorityQueue().index(29) + 1)      # + 1, because of 1-based indexing!
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(29)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.remove(pq.getPriorityQueue().index(29) + 1)      # + 1, because of 1-based indexing!
    pq.insert(70)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    print("Max element: {}".format(pq.extractMax()))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(pq.getPriorityQueue().index(15) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    try:
        pq.remove(pq.getPriorityQueue().index(150) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(pq.getPriorityQueue().index(70) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(200)
    except Exception as e:
        print(e)
    try:
        pq.remove(10)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.printHeap()

    pq.changePriority(10, 50)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.printHeap()



def testMinPriorityQueue(elts, maxSize):
    
    pq = Heaps.MinPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        print("Min element: {}".format(pq.extractMin()))
    except Exception as e:
        print(e)
    try:
        pq.remove(0)
    except Exception as e:
        print(e)
    try:
        pq.remove(1)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(100)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    print("Min element: {}".format(pq.extractMin()))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(123)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(1)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    size = len(elts)
    for i in range(size):
        pq.insert(elts[i])
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    pq.insert(17)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    pq.insert(17)
    try:
        pq.insert(123)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.insert(50)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.remove(pq.getPriorityQueue().index(29) + 1)      # + 1, because of 1-based indexing!
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(29)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.remove(pq.getPriorityQueue().index(29) + 1)      # + 1, because of 1-based indexing!
    pq.insert(70)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    print("Min element: {}".format(pq.extractMin()))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(pq.getPriorityQueue().index(15) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    try:
        pq.remove(pq.getPriorityQueue().index(150) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(pq.getPriorityQueue().index(70) + 1)      # + 1, because of 1-based indexing!
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(70)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.remove(200)
    except Exception as e:
        print(e)
    try:
        pq.remove(10)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.printHeap()

    pq.insert(5)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.insert(15)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.remove(pq.getPriorityQueue().index(15) + 1)      # + 1, because of 1-based indexing!
    pq.insert(10)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.printHeap()

    pq.changePriority(11, 6)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    pq.printHeap()



"""Sorting Algorithms"""

def testHeapSort1(A, maxSize):

    pq = Heaps.MaxPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    n = len(A)

    try:
        pq.buildHeap(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.heapSortNonDescending(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()

def testHeapSort2(A, maxSize):

    pq = Heaps.MaxPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    n = len(A)

    try:
        pq.buildHeap(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.heapSortNonAscending(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()

def testHeapSort3(A, maxSize):

    pq = Heaps.MinPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    n = len(A)

    try:
        pq.buildHeap(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.heapSortNonDescending(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()

def testHeapSort4(A, maxSize):

    pq = Heaps.MinPriorityQueue(maxSize)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    n = len(A)

    try:
        pq.buildHeap(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print()

    try:
        pq.heapSortNonAscending(A, n)
    except Exception as e:
        print(e)
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()


def heapSort1(A, maxSize):
    """Creates a heap from the array A.
       maxSize is the maximum size for the heap.
       Then it sorts the array in non-descending order and returns it as sorted.
       Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
    """
    pq = Heaps.MaxPriorityQueue(maxSize)
    n = len(A)
    for i in range(n):
        pq.insert(A[i])
    for i in range(n-1, -1, -1):       # range(n) for non-ascending order
        A[i] = pq.extractMax()
    return A

def heapSort2(A, maxSize):
    """Creates a heap from the array A.
       maxSize is the maximum size for the heap.
       Then it sorts the array in non-descending order and returns it as sorted.
       Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
    """
    pq = Heaps.MinPriorityQueue(maxSize)
    n = len(A)
    for i in range(n):
        pq.insert(A[i])
    for i in range(n):       # range(n-1, -1, -1) for non-ascending order
        A[i] = pq.extractMin()
    return A



"""Partial Sorting"""

def testPartialSortingMax(A, k, maxSize):

    pq = Heaps.MaxPriorityQueue(maxSize)

    n = len(A)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()

    print()
    print(pq.partialSortingMax(A, n, k))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()


def testPartialSortingMin(A, k, maxSize):

    pq = Heaps.MinPriorityQueue(maxSize)

    n = len(A)

    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()

    print()
    print(pq.partialSortingMin(A, n, k))
    print(pq.getPriorityQueue())
    print("Size, Max Size:", pq.getSize(), pq.getMaxSize())
    print("Tree:")
    print(pq)
    print(A)
    print()


if __name__ == "__main__":
    elts = [11, 13, 12, 18, 14, 42, 7, 18, 29]      # len(elts) = 9
    #elts = [42, 29, 18, 14, 7, 18, 12, 11, 13]     # len(elts) = 9

    maxSize = 13    # Try with 13 (valid), and 3 (invalid). Also try with 9, which is a border case, but it's valid.

    n = len(elts)
    k = n                                       # Test with boundary cases, especially with k = n.

    testMaxPriorityQueue(elts, maxSize)
    #testMinPriorityQueue(elts, maxSize)

    """ Sorting algorithms"""
    #A = elts[:]
    #testHeapSort1(A, maxSize)           # Sorts the array in place! A will be sorted after this!
    #print(A, elts)

    #A = elts[:]
    #testHeapSort2(A, maxSize)           # Sorts the array in place! A will be sorted after this!
    #print(A, elts)

    #A = elts[:]
    #testHeapSort3(A, maxSize)           # Sorts the array in place! A will be sorted after this!
    #print(A, elts)

    #A = elts[:]
    #testHeapSort4(A, maxSize)           # Sorts the array in place! A will be sorted after this!
    #print(A, elts)


    #A = elts[:]
    #print(heapSort1(A, maxSize), A)     # Sorts the array in place! A will be sorted after this!
    #print(elts)

    #A = elts[:]
    #print(heapSort2(A, maxSize), A)     # Sorts the array in place! A will be sorted after this!
    #print(elts)

    """Partial Sorting"""
    #A = elts[:]
    #testPartialSortingMax(A, k, maxSize)
    #print(A, elts)
    #print()

    #A = elts[:]
    #testPartialSortingMin(A, k, maxSize)
    #print(A, elts)
    #print()
