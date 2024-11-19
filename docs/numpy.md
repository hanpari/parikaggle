# NumPy: A Comprehensive Overview

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

## Key Features

- **N-dimensional array object (ndarray)**: Efficiently stores large datasets.
- **Broadcasting**: Handles arithmetic operations on arrays of different shapes.
- **Universal functions (ufuncs)**: Perform element-wise operations on arrays.
- **Linear algebra, Fourier transform, and random number capabilities**.
- **Integration with other libraries**: Works seamlessly with libraries like Pandas, SciPy, and Matplotlib.

## Installation

To install NumPy, use pip:

```bash
pip install numpy
```

## Basic Usage

### Importing NumPy

```python
import numpy as np
```

### Creating Arrays

#### 1D Array

```python
a = np.array([1, 2, 3])
print(a)
```

#### 2D Array

```python
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print(b)
```

#### 3D Array

```python
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)
print(c)
```

### Initial Placeholders

#### Array of Zeros

```python
zeros = np.zeros((3, 4))
print(zeros)
```

#### Array of Ones

```python
ones = np.ones((2, 3, 4), dtype=np.int16)
print(ones)
```

### Array Operations

#### Arithmetic Operations

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
```

#### Statistical Operations

```python
data = np.array([1, 2, 3, 4, 5])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
```

### Reshaping Arrays

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
reshaped = arr.reshape(3, 2)
print(reshaped)
```

### Indexing and Slicing

```python
arr = np.array([1, 2, 3, 4, 5])

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice:", arr[1:4])
```

### Broadcasting

```python
a = np.array([1, 2, 3])
b = np.array([4])

print(a + b)  # Broadcasting adds 4 to each element of array a
```

### Linear Algebra

```python
from numpy.linalg import inv, qr

matrix = np.array([[1, 2], [3, 4]])
print("Inverse:\n", inv(matrix))
q, r = qr(matrix)
print("QR Decomposition:\nQ:\n", q, "\nR:\n", r)
```

### Random Numbers

```python
random_array = np.random.random((2, 2))
print(random_array)
```

## Conclusion

NumPy is a powerful library that forms the foundation for many other scientific computing libraries in Python. Its efficient array operations and extensive functionality make it an essential tool for data analysis and manipulation.

---

Feel free to experiment with these examples and explore more features of NumPy! If you have any questions or need further assistance, just let me know.

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) NumPy Cheat Sheet: Data Analysis in Python | DataCamp. <https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python>.
(2) NumPy Tutorial: Your First Steps Into Data Science in Python. <https://realpython.com/numpy-tutorial/>.
(3) NumPy: the absolute basics for beginners — NumPy v2.1 Manual. <https://numpy.org/doc/stable/user/absolute_beginners.html>.
(4) github.com. <https://github.com/Cstevenlopez/PRACTICA_3/tree/68b01b3ad3bcdb429bbf35b8bc8057fbf9a45766/md%2FCuaderno%232.md>.
