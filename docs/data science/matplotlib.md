# Matplotlib: A Comprehensive Overview

Matplotlib is a widely-used plotting library for Python, providing a flexible and comprehensive way to create static, animated, and interactive visualizations.

## Key Features

- **Versatile Plotting**: Supports a wide range of plots including line, bar, scatter, histogram, and more.
- **Customization**: Extensive options to customize plots (colors, labels, grids, etc.).
- **Integration**: Works well with NumPy, Pandas, and other scientific libraries.
- **Interactive Plots**: Capabilities for interactive plots in Jupyter Notebooks and other environments.

## Installation

To install Matplotlib, use pip:

```bash
pip install matplotlib
```

## Basic Usage

### Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

### Creating Simple Plots

#### Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

#### Scatter Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### Customizing Plots

#### Adding Legends and Annotations

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sine')
plt.plot(x, y2, label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.annotate('Max', xy=(1.57, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

#### Changing Colors and Styles

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, 'r--')  # Red dashed line
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### Subplots

#### Creating Multiple Plots

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x, y1)
ax1.set_title('Sine Wave')
ax2.plot(x, y2)
ax2.set_title('Cosine Wave')
plt.tight_layout()
plt.show()
```

### Histograms

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.5, color='g')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Saving Plots

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('sine_wave.png')
plt.show()
```

## Conclusion

Matplotlib is a versatile and powerful library for creating a wide range of static, animated, and interactive plots in Python. Its extensive customization options and integration with other libraries make it an essential tool for data visualization.

---

Feel free to experiment with these examples and explore more features of Matplotlib! If you have any questions or need further assistance, just let me know.

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) Matplotlib cheatsheets — Visualization with Python. <https://matplotlib.org/cheatsheets/>.
(2) Examples — Matplotlib 3.9.2 documentation. <https://matplotlib.org/stable/gallery/index.html>.
(3) Top 50 matplotlib Visualizations - The Master Plots (w/ Full Python .... <https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/>.
