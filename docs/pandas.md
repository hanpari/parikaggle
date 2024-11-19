# Pandas: A Comprehensive Overview

Pandas is a powerful, open-source data analysis and manipulation library for Python. It provides data structures and functions needed to work with structured data seamlessly.

## Key Features

- **DataFrame and Series**: Primary data structures for handling tabular and time series data.
- **Data Cleaning**: Functions to handle missing data, duplicate data, and data transformation.
- **Data Aggregation and Grouping**: Tools for summarizing data.
- **Time Series Analysis**: Functions for date and time manipulation.
- **Integration with other libraries**: Works well with NumPy, Matplotlib, and more.

## Installation

To install Pandas, use pip:

```bash
pip install pandas
```

## Basic Usage

### Importing Pandas

```python
import pandas as pd
```

### Creating Data Structures

#### Series

A Series is a one-dimensional array-like object.

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
```

#### DataFrame

A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data.

```python
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)
```

### Reading and Writing Data

#### Reading CSV

```python
df = pd.read_csv('data.csv')
print(df.head())
```

#### Writing to CSV

```python
df.to_csv('output.csv', index=False)
```

### Data Selection

#### Selecting Columns

```python
print(df['Name'])
```

#### Selecting Rows

```python
print(df.iloc[0])  # By index
print(df.loc[0])   # By label
```

### Data Cleaning

#### Handling Missing Data

```python
df.dropna(inplace=True)  # Drop rows with missing values
df.fillna(0, inplace=True)  # Fill missing values with 0
```

#### Removing Duplicates

```python
df.drop_duplicates(inplace=True)
```

### Data Aggregation and Grouping

#### Grouping Data

```python
grouped = df.groupby('City')
print(grouped.mean())
```

#### Aggregating Data

```python
print(df['Age'].sum())
print(df['Age'].mean())
```

### Time Series Analysis

#### Creating a Time Series

```python
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
```

#### Resampling

```python
ts = df['A'].cumsum()
print(ts.resample('M').mean())
```

### Merging and Joining

#### Concatenating DataFrames

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']})
df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5']})
result = pd.concat([df1, df2])
print(result)
```

#### Merging DataFrames

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})
merged = pd.merge(left, right, on='key')
print(merged)
```

## Conclusion

Pandas is an essential tool for data analysis and manipulation in Python. Its robust data structures and versatile functions make it a go-to library for handling structured data efficiently.

---

Feel free to experiment with these examples and explore more features of Pandas! If you have any questions or need further assistance, just let me know.

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) Summarizing and Analyzing a Pandas DataFrame • datagy. <https://datagy.io/pandas-exploratory-data-analysis/>.
(2) pandas.DataFrame.to_markdown — pandas 2.2.3 documentation. <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_markdown.html>.
(3) Using expandable content on GitHub with Markdown #details #summary # .... <https://gist.github.com/scmx/eca72d44afee0113ceb0349dd54a84a2>.
(4) 5 Best Ways to Summarize Statistics of a Pandas DataFrame in ... - Finxter. <https://blog.finxter.com/5-best-ways-to-summarize-statistics-of-a-pandas-dataframe-in-python/>.
(5) undefined. <https://raw.githubusercontent.com/datagy/data/main/sales.csv>.
