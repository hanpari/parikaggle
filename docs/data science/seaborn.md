# Seaborn: A Comprehensive Overview

Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Key Features

- **Built on Matplotlib**: Provides a high-level interface for drawing attractive statistical graphics.
- **Integration with Pandas**: Works seamlessly with Pandas data structures.
- **Themes and Color Palettes**: Offers built-in themes and color palettes to make plots more visually appealing.
- **Complex Plots Made Simple**: Simplifies the process of creating complex visualizations like heatmaps, time series, and violin plots.

## Installation

To install Seaborn, use pip:

```bash
pip install seaborn
```

## Basic Usage

### Importing Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Example Datasets

Seaborn comes with several built-in datasets that you can use for practice and learning.

```python
# Load an example dataset
tips = sns.load_dataset("tips")
print(tips.head())
```

### Basic Plotting

#### Scatter Plot

```python
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()
```

#### Line Plot

```python
sns.lineplot(x="size", y="total_bill", data=tips)
plt.title('Line Plot of Size vs Total Bill')
plt.show()
```

### Statistical Plots

#### Box Plot

```python
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('Box Plot of Total Bill by Day')
plt.show()
```

#### Violin Plot

```python
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title('Violin Plot of Total Bill by Day')
plt.show()
```

### Distribution Plots

#### Histogram

```python
sns.histplot(tips['total_bill'], bins=30, kde=True)
plt.title('Histogram of Total Bill')
plt.show()
```

#### KDE Plot

```python
sns.kdeplot(tips['total_bill'], shade=True)
plt.title('KDE Plot of Total Bill')
plt.show()
```

### Categorical Plots

#### Bar Plot

```python
sns.barplot(x="day", y="total_bill", data=tips)
plt.title('Bar Plot of Total Bill by Day')
plt.show()
```

#### Count Plot

```python
sns.countplot(x="day", data=tips)
plt.title('Count Plot of Days')
plt.show()
```

### Matrix Plots

#### Heatmap

```python
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d")
plt.title('Heatmap of Flight Passengers')
plt.show()
```

### Pair Plot

```python
sns.pairplot(tips)
plt.title('Pair Plot of Tips Dataset')
plt.show()
```

### Customizing Plots

#### Changing Themes

```python
sns.set_theme(style="darkgrid")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title('Scatter Plot with Darkgrid Theme')
plt.show()
```

#### Custom Color Palettes

```python
sns.set_palette("husl")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title('Box Plot with Custom Color Palette')
plt.show()
```

## Conclusion

Seaborn is a powerful and user-friendly library for creating beautiful and informative statistical graphics in Python. Its integration with Pandas and Matplotlib, along with its high-level interface, makes it an essential tool for data visualization.

---

Feel free to experiment with these examples and explore more features of Seaborn! If you have any questions or need further assistance, just let me know.

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) Example gallery — seaborn 0.13.2 documentation. <https://seaborn.pydata.org/examples/index.html>.
(2) Using expandable content on GitHub with Markdown #details #summary # .... <https://gist.github.com/scmx/eca72d44afee0113ceb0349dd54a84a2>.
(3) Visualizing Data in Python With Seaborn. <https://realpython.com/python-seaborn/>.
(4) undefined. <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details>.
(5) undefined. <https://caniuse.com/>.
(6) undefined. <https://gist.github.com/ericclemmons/b146fe5da72ca1f706b2ef72a20ac39d>.
