"""
 Heaps are Complete Binary Trees.

 The Complete Binary Max-Heap is implemented as an array, which is both fast and memory efficient. It's also easy to code.
 The code uses 1-based indexing, not 0-based.
 That's why it will ignore the element at position i == 0, and will have actual size larger by one.

 Priority Queues are usually implemented as Heaps.
"""

class Heap(object):
    """The Complete Binary Heap"""

    def __init__(self, maxSize):
        """The Complete Binary Heap
        Instantiates an array of size maxSize that holds the elements of the heap.
        Input: maxSize
        Contains property named size that holds the current size of the heap, which is at most equal to maxSize.
        """
        self.H = [None] * (maxSize + 1)     # H is the array (a Python list) that stores the heap. Its first element, at index 0, is ignored.
                                            # H[1 . . . maxSize] is an array of length maxSize where the heap occupies the first size elements.
        self.size = 0                       # size is the current size of the heap. Its first element, at index 0, is ignored.
        self.maxSize = maxSize              # maxSize is the maximum number of elements in the heap. Its first element, at index 0, is ignored.

    def parent(self, i):
        return i // 2

    def leftChild(self, i):
        return 2*i

    def rightChild(self, i):
        return 2*i + 1

    def insert(self, val):
        """Inserts a new element with value val into the heap, if there is space.
           Input: val
           O(log n)
        """
        if self.size == self.maxSize:
            raise Exception("The heap is full! Cannot insert the element with value {}.".format(val))
        self.size += 1
        self.H[self.size] = val
        self.siftUp(self.size)

    def getHeap(self):
        """Returns the array H[1, size] that represents the heap."""
        return self.H[1 : self.size + 1]

    def getSize(self):
        """Returns the current size of the heap."""
        return self.size

    def getMaxSize(self):
        """Returns the maximum size of the heap."""
        return self.maxSize

    def buildHeap(self, A, n):
        """Creates a heap from the array A with length n.
           Inputs: A, n
           Its time complexity is actually O(2n), which is O(n), but it uses additional space for storing the heap, O(n).
        """
        if n > self.maxSize:
            raise Exception("Length of array A ({}) must not exceed maxSize of the heap ({})!".format(n, self.maxSize))
        self.size = n       # n = len(A)
        self.H = [None] + A
        #self.H[1:] = A     # It's the same.
        for i in range(n//2, 0, -1):
            self.siftDown(i)

    def printHeap(self):
        """Prints the heap as a complete binary tree.
           Prints all nodes followed by their children.
        """
        result = ""
        for i in range(1, self.size + 1):
            result += str(self.H[i]) + ": "
            if self.leftChild(i) <= self.size:
                result += str(self.H[self.leftChild(i)]) + " "
            else:
                result += "* "
            if self.rightChild(i) <= self.size:
                result += str(self.H[self.rightChild(i)])
            else:
                result += "*"
            result += "\n"
        print(result)

    def __str__(self):
        """Prints the heap as a complete binary tree.
           Uses Breadth First Search.
        """
        from collections import deque
        import math
        result = ""
        if self.size > 0:
            maxLevel = int(math.log(self.size, 2))
            queue = deque([1])    # Index of root node. That's the element with the highest value(priority) in case of MaxHeap, or with the lowest value(priority) in case of MinHeap.
        else:
            maxLevel = 1
            queue = []
        bounds = [2**j - 1 for j in range(1, maxLevel + 1)]
        while len(queue):
            i = queue.popleft()
            result += str(self.H[i]) + " "
            if self.leftChild(i) <= self.size:
                queue.append(self.leftChild(i))
            if self.rightChild(i) <= self.size:
                queue.append(self.rightChild(i))
            if i % 2:
                result += "\t"      # This is a complete binary tree!
            if i in bounds:
                result += "\n"
        return result



class MaxHeap(Heap):
    """The Complete Binary Max-Heap"""

    def __init__(self, maxSize):
        """The Complete Binary Max-Heap
        Instantiates an array of size maxSize that holds the elements of the heap.
        Input: maxSize
        Contains property named size that holds the current size of the heap, which is at most equal to maxSize.
        """
        return super(MaxHeap, self).__init__(maxSize)

    def siftUp(self, i):
        """Sifts the element with index i up until it finds its place.
           Used internally (privately) in the class.
           O(log n)
        """
        while i > 1 and self.H[self.parent(i)] < self.H[i]:    # Root is at i == 1.
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)

    def siftDown(self, i):
        """Sifts the element with index i down until it finds its place.
           Used internally (privately) in the class.
           O(log n)
        """
        while i <= self.size:
            maxIndex = i
            l = self.leftChild(i)
            if l <= self.size and self.H[l] > self.H[maxIndex]:
                maxIndex = l
            r = self.rightChild(i)
            if r <= self.size and self.H[r] > self.H[maxIndex]:
                maxIndex = r
            if i != maxIndex:
                self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
                i = maxIndex
            else:
                break

    def siftDownRecursive(self, i):
        """Sifts the element with index i down until it finds its place.
           Recursive implementation.
           Used internally (privately) in the class.
           O(log n)
        """
        maxIndex = i
        l = self.leftChild(i)
        if l <= self.size and self.H[l] > self.H[maxIndex]:
            maxIndex = l
        r = self.rightChild(i)
        if r <= self.size and self.H[r] > self.H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
            self.siftDownRecursive(maxIndex)

    def extractMax(self):
        """Returns the element with the highest value (priority).
           O(log n)"""
        if self.size >= 1:
            result = self.H[1]
            self.H[1] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)
            return result
        else:
            raise Exception("The heap is empty! Cannot return the element with the highest value.")

    def remove(self, i):
        """Removes the element with index i.
           Input: i
           O(log n)"""
        if i <= self.size:
            self.H[i] = float("inf")
            self.siftUp(i)
            self.extractMax()
        else:
            raise Exception("No element with index {}!".format(i))

    def changeValue(self, i, val):
        """Changes the value of the element with index i.
           Inputs: i, val
           O(log n)"""
        oldVal = self.H[i]
        self.H[i] = val
        if val > oldVal:
            self.siftUp(i)
        else:
            self.siftDown(i)

    def heapSortNonDescending(self, A, n):
        """Creates a heap from the array A with length n.
           Then it sorts the array A in non-descending order in-place.
           Inputs: A, n
           It doesn't return A, because it sorts it in-place.
           Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
        """
        self.buildHeap(A, n)
        for _ in range(n):
            self.H[1], self.H[self.size] = self.H[self.size], self.H[1]
            A[self.size-1] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)

    def heapSortNonAscending(self, A, n):
        """Creates a heap from the array A with length n.
           Then it sorts the array A in non-ascending order in-place.
           Inputs: A, n
           It doesn't return A, because it sorts it in-place.
           Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
        """
        self.buildHeap(A, n)
        for i in range(n):
            self.H[1], self.H[self.size] = self.H[self.size], self.H[1]
            A[i] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)

    def partialSortingMax(self, A, n, k):
        """Inputs: Array A[1, n]; n, which is len(A); Integer k, such that 1 <= k <= n
           Output: The last (maximal) k elements of a sorted version of A.
           O(n), if k <= O(n/log n)
        """
        assert 1 <= k <= n
        self.buildHeap(A, n)
        result = []
        for i in range(k):
            result.append(self.extractMax())
        return result



class MinHeap(Heap):
    """The Complete Binary Min-Heap"""

    def __init__(self, maxSize):
        """The Complete Binary Min-Heap
        Instantiates an array of size maxSize that holds the elements of the heap.
        Input: maxSize
        Contains property named size that holds the current size of the heap, which is at most equal to maxSize.
        """
        return super(MinHeap, self).__init__(maxSize)

    def siftUp(self, i):
        """Sifts the element with index i up until it finds its place.
           Used internally (privately) in the class.
           O(log n)
        """
        while i > 1 and self.H[self.parent(i)] > self.H[i]:    # Root is at i == 1.
            self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
            i = self.parent(i)

    def siftDown(self, i):
        """Sifts the element with index i down until it finds its place.
           Used internally (privately) in the class.
           O(log n)
        """
        while i <= self.size:
            maxIndex = i
            l = self.leftChild(i)
            if l <= self.size and self.H[l] < self.H[maxIndex]:
                maxIndex = l
            r = self.rightChild(i)
            if r <= self.size and self.H[r] < self.H[maxIndex]:
                maxIndex = r
            if i != maxIndex:
                self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
                i = maxIndex
            else:
                break

    def siftDownRecursive(self, i):
        """Sifts the element with index i down until it finds its place.
           Recursive implementation.
           Used internally (privately) in the class.
           O(log n)
        """
        maxIndex = i
        l = self.leftChild(i)
        if l <= self.size and self.H[l] < self.H[maxIndex]:
            maxIndex = l
        r = self.rightChild(i)
        if r <= self.size and self.H[r] < self.H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
            self.siftDownRecursive(maxIndex)

    def extractMin(self):
        """Returns the element with the lowest value (priority).
           O(log n)"""
        if self.size >= 1:
            result = self.H[1]
            self.H[1] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)
            return result
        else:
            raise Exception("The heap is empty! Cannot return the element with the lowest value.")

    def remove(self, i):
        """Removes the element with index i.
           Input: i
           O(log n)"""
        if i <= self.size:
            self.H[i] = float("-inf")
            self.siftUp(i)
            self.extractMin()
        else:
            raise Exception("No element with index {}!".format(i))

    def changeValue(self, i, val):
        """Changes the value of the element with index i.
           Inputs: i, val
           O(log n)"""
        oldVal = self.H[i]
        self.H[i] = val
        if val > oldVal:
            self.siftDown(i)
        else:
            self.siftUp(i)

    def heapSortNonDescending(self, A, n):
        """Creates a heap from the array A with length n.
           Then it sorts the array A in non-descending order in-place.
           Inputs: A, n
           It doesn't return A, because it sorts it in-place.
           Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
        """
        self.buildHeap(A, n)
        for i in range(n):
            self.H[1], self.H[self.size] = self.H[self.size], self.H[1]
            A[i] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)

    def heapSortNonAscending(self, A, n):
        """Creates a heap from the array A with length n.
           Then it sorts the array A in non-ascending order in-place.
           Inputs: A, n
           It doesn't return A, because it sorts it in-place.
           Its time complexity is O(n log n), but it uses additional space for storing the heap, O(n).
        """
        self.buildHeap(A, n)
        for _ in range(n):
            self.H[1], self.H[self.size] = self.H[self.size], self.H[1]
            A[self.size-1] = self.H[self.size]
            self.size -= 1
            self.siftDown(1)

    def partialSortingMin(self, A, n, k):
        """Inputs: Array A[1, n]; n, which is len(A); Integer k, such that 1 <= k <= n
           Output: The last (minimal) k elements of a sorted version of A.
           O(n), if k <= O(n/log n)
        """
        assert 1 <= k <= n
        self.buildHeap(A, n)
        result = []
        for i in range(k):
            result.append(self.extractMin())
        return result



class MaxPriorityQueue(MaxHeap):
    """Priority Queue implemented as The Complete Binary Max-Heap"""

    def __init__(self, maxSize):
        """Priority Queue implemented as The Complete Binary Max-Heap
        Instantiates an array of size maxSize that holds the elements of the priority queue.
        Inherits from class MaxHeap, and is practically identical to it.
        Input: maxSize
        Contains property named size that holds the current size of the priority queue, which is at most equal to maxSize.
        """
        return super(MaxPriorityQueue, self).__init__(maxSize)

    def insert(self, p):        # p stands for priority. That's the value of an element.
        """Inserts a new element with priority p into the heap, if there is space.
           Input: p
           O(log n)"""
        return super(MaxPriorityQueue, self).insert(p)

    def changePriority(self, i, p):
        """Changes the priority p of the element with index i.
           Inputs: i, p
           O(log n)"""
        return super(MaxPriorityQueue, self).changeValue(i, p)

    def getPriorityQueue(self):
        """Returns the array H[1, size] that represents the priority queue."""
        return super(MaxPriorityQueue, self).getHeap()



class MinPriorityQueue(MinHeap):
    """Priority Queue implemented as The Complete Binary Min-Heap"""

    def __init__(self, maxSize):
        """Priority Queue implemented as The Complete Binary Min-Heap
        Instantiates an array of size maxSize that holds the elements of the priority queue.
        Inherits from class MinHeap, and is practically identical to it.
        Input: maxSize
        Contains property named size that holds the current size of the priority queue, which is at most equal to maxSize.
        """
        return super(MinPriorityQueue, self).__init__(maxSize)

    def insert(self, p):        # p stands for priority. That's the value of an element.
        """Inserts a new element with priority p into the heap, if there is space.
           Input: p
           O(log n)"""
        return super(MinPriorityQueue, self).insert(p)

    def changePriority(self, i, p):
        """Changes the priority p of the element with index i.
           Inputs: i, p
           O(log n)"""
        return super(MinPriorityQueue, self).changeValue(i, p)

    def getPriorityQueue(self):
        """Returns the array H[1, size] that represents the priority queue."""
        return super(MinPriorityQueue, self).getHeap()
