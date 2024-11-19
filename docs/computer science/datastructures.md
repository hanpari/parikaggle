## Data Structures

### 1. Arrays

**Description**: An array is a collection of elements identified by index or key. It is one of the simplest data structures and is used to store a fixed-size sequential collection of elements of the same type.

**Characteristics**:

- **Access Time**: $$O(1)$$
- **Search Time**: $$O(n)$$
- **Insertion Time**: $$O(n)$$
- **Deletion Time**: $$O(n)$$
- **Fixed Size**: Yes

**Pseudocode**:

```plaintext
function createArray(size):
    array = new Array[size]
    return array

function accessElement(array, index):
    return array[index]

function updateElement(array, index, value):
    array[index] = value
```

### 2. Linked Lists

**Description**: A linked list is a linear data structure where each element is a separate object, called a node. Each node contains data and a reference (or link) to the next node in the sequence.

**Characteristics**:

- **Access Time**: $$O(n)$$
- **Search Time**: $$O(n)$$
- **Insertion Time**: $$O(1)$$
- **Deletion Time**: $$O(1)$$
- **Dynamic Size**: Yes

**Pseudocode**:

```plaintext
class Node:
    data
    next

function createLinkedList():
    head = null
    return head

function insertAtBeginning(head, data):
    newNode = new Node()
    newNode.data = data
    newNode.next = head
    head = newNode
    return head

function deleteNode(head, key):
    temp = head
    if temp != null and temp.data == key:
        head = temp.next
        return head
    while temp != null and temp.next.data != key:
        temp = temp.next
    if temp == null:
        return head
    temp.next = temp.next.next
    return head
```

### 3. Stacks

**Description**: A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The operations are performed at one end, called the top of the stack.

**Characteristics**:

- **Access Time**: $$O(n)$$
- **Search Time**: $$O(n)$$
- **Insertion Time**: $$O(1)$$
- **Deletion Time**: $$O(1)$$
- **Dynamic Size**: Yes

**Pseudocode**:

```plaintext
class Stack:
    items = []

function push(stack, item):
    stack.items.append(item)

function pop(stack):
    if not isEmpty(stack):
        return stack.items.pop()

function isEmpty(stack):
    return len(stack.items) == 0
```

### 4. Queues

**Description**: A queue is a linear data structure that follows the First In First Out (FIFO) principle. The operations are performed at both ends, with insertion at the rear and deletion at the front.

**Characteristics**:

- **Access Time**: $$O(n)$$
- **Search Time**: $$O(n)$$
- **Insertion Time**: $$O(1)$$
- **Deletion Time**: $$O(1)$$
- **Dynamic Size**: Yes

**Pseudocode**:

```plaintext
class Queue:
    items = []

function enqueue(queue, item):
    queue.items.append(item)

function dequeue(queue):
    if not isEmpty(queue):
        return queue.items.pop(0)

function isEmpty(queue):
    return len(queue.items) == 0
```

### 5. Trees

**Description**: A tree is a hierarchical data structure consisting of nodes, with a single node as the root. Each node has zero or more child nodes, and nodes with no children are called leaves.

**Characteristics**:

- **Access Time**: $$O(\log n)$$
- **Search Time**: $$O(\log n)$$
- **Insertion Time**: $$O(\log n)$$
- **Deletion Time**: $$O(\log n)$$
- **Dynamic Size**: Yes

**Pseudocode**:

```plaintext
class TreeNode:
    data
    left
    right

function insertNode(root, data):
    if root == null:
        root = new TreeNode()
        root.data = data
    elif data < root.data:
        root.left = insertNode(root.left, data)
    else:
        root.right = insertNode(root.right, data)
    return root

function searchNode(root, data):
    if root == null or root.data == data:
        return root
    if data < root.data:
        return searchNode(root.left, data)
    return searchNode(root.right, data)
```

### 6. Graphs

**Description**: A graph is a collection of nodes (vertices) and edges connecting pairs of nodes. Graphs can be directed or undirected, and they can be weighted or unweighted.

**Characteristics**:

- **Access Time**: $$O(1)$$
- **Search Time**: $$O(V + E)$$
- **Insertion Time**: $$O(1)$$
- **Deletion Time**: $$O(V + E)$$
- **Dynamic Size**: Yes

**Pseudocode**:

```plaintext
class Graph:
    adjList = {}

function addVertex(graph, vertex):
    if vertex not in graph.adjList:
        graph.adjList[vertex] = []

function addEdge(graph, vertex1, vertex2):
    if vertex1 in graph.adjList and vertex2 in graph.adjList:
        graph.adjList[vertex1].append(vertex2)
        graph.adjList[vertex2].append(vertex1)

function bfs(graph, startVertex):
    visited = set()
    queue = [startVertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([v for v in graph.adjList[vertex] if v not in visited])
    return visited
```

These are some of the main data structures, each with its own unique characteristics and use cases. If you have any specific questions or need further details, feel free to ask!

Zdroj: konverzace s Copilotem, 19. 11. 2024
(1) Pseudocode Cheat Sheet - Ryan's Tutorials. <https://ryanstutorials.net/software-design-and-development/algorithms-pseudocode-summary.php>.
(2) Pseudocodes (Guidelines, Advantages & Disadvantages). <https://www.codesansar.com/computer-basics/pseudocodes.htm>.
(3) What is Pseudocode: Use Cases and Examples - PseudoEditor. <https://pseudoeditor.com/guides/what-is-pseudocode>.
(4) Pseudocode: What It Is and How to Write It - Built In. <https://builtin.com/data-science/pseudocode>.
