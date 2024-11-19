## Sorting Algorithms

### 1. Bubble Sort

**Description**: Bubble Sort is a simple comparison-based algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n)$$
  - Average: $$O(n^2)$$
  - Worst: $$O(n^2)$$
- **Space Complexity**: $$O(1)$$
- **Stable**: Yes
- **In-Place**: Yes

**Pseudocode**:

```plaintext
function bubbleSort(arr):
    n = length(arr)
    for i from 0 to n-1:
        for j from 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
    return arr
```

### 2. Selection Sort

**Description**: Selection Sort divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swaps it with the leftmost unsorted element, and moves the sublist boundaries one element to the right.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n^2)$$
  - Average: $$O(n^2)$$
  - Worst: $$O(n^2)$$
- **Space Complexity**: $$O(1)$$
- **Stable**: No
- **In-Place**: Yes

**Pseudocode**:

```plaintext
function selectionSort(arr):
    n = length(arr)
    for i from 0 to n-1:
        minIndex = i
        for j from i+1 to n:
            if arr[j] < arr[minIndex]:
                minIndex = j
        swap(arr[i], arr[minIndex])
    return arr
```

### 3. Insertion Sort

**Description**: Insertion Sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n)$$
  - Average: $$O(n^2)$$
  - Worst: $$O(n^2)$$
- **Space Complexity**: $$O(1)$$
- **Stable**: Yes
- **In-Place**: Yes

**Pseudocode**:

```plaintext
function insertionSort(arr):
    n = length(arr)
    for i from 1 to n-1:
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
```

### 4. Merge Sort

**Description**: Merge Sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, meaning that the implementation preserves the input order of equal elements in the sorted output.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n \log n)$$
  - Average: $$O(n \log n)$$
  - Worst: $$O(n \log n)$$
- **Space Complexity**: $$O(n)$$
- **Stable**: Yes
- **In-Place**: No

**Pseudocode**:

```plaintext
function mergeSort(arr):
    if length(arr) > 1:
        mid = length(arr) // 2
        leftHalf = arr[0:mid]
        rightHalf = arr[mid:length(arr)]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = j = k = 0

        while i < length(leftHalf) and j < length(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < length(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < length(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    return arr
```

### 5. Quick Sort

**Description**: Quick Sort is an efficient, in-place, comparison-based, divide and conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n \log n)$$
  - Average: $$O(n \log n)$$
  - Worst: $$O(n^2)$$
- **Space Complexity**: $$O(\log n)$$
- **Stable**: No
- **In-Place**: Yes

**Pseudocode**:

```plaintext
function quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

function partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j from low to high - 1:
        if arr[j] < pivot:
            i += 1
            swap(arr[i], arr[j])
    swap(arr[i + 1], arr[high])
    return i + 1
```

### 6. Heap Sort

**Description**: Heap Sort is a comparison-based sorting technique based on a binary heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

**Characteristics**:

- **Time Complexity**:
  - Best: $$O(n \log n)$$
  - Average: $$O(n \log n)$$
  - Worst: $$O(n \log n)$$
- **Space Complexity**: $$O(1)$$
- **Stable**: No
- **In-Place**: Yes

**Pseudocode**:

```plaintext
function heapSort(arr):
    n = length(arr)

    for i from n // 2 - 1 to 0:
        heapify(arr, n, i)

    for i from n-1 to 0:
        swap(arr[0], arr[i])
        heapify(arr, i, 0)

function heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr[i], arr[largest])
        heapify(arr, n, largest)
```

These are some of the main sorting algorithms, each with its own unique characteristics and use cases. If you have any specific questions or need further details, feel free to ask!

Zdroj: konverzace s Copilotem, 19. 11. 2024
(1) Sorting Algorithms [Ultimate Guide] - HappyCoders.eu. <https://www.happycoders.eu/algorithms/sorting-algorithms/>.
(2) Advanced Notes - 2.3.1 Sorting Algorithms - Physics & Maths Tutor. <https://pmt.physicsandmathstutor.com/download/Computer-Science/A-level/Notes/OCR/2.3-Algorithms/Advanced/2.3.3.%20Sorting%20Algorithms.pdf>.
(3) Sorting Algorithms Explained - freeCodeCamp.org. <https://www.freecodecamp.org/news/sorting-algorithms-explained/>.
(4) Sorting Algorithm - Programiz. <https://www.programiz.com/dsa/sorting-algorithm>.
(5) github.com. <https://github.com/devil-cyber/Data-Structure-Algorithm/tree/b3e09a6e97c553f968fd98dd5988264d1e67ef82/heap%2Fheapsort.py>.
