# NetworkX: A Comprehensive Overview

NetworkX is a powerful Python library for the creation, manipulation, and study of complex networks of nodes and edges. It is widely used for network analysis and visualization in various fields such as social network analysis, biology, computer science, and more.

## Key Features

- **Graph Types**: Supports various types of graphs including undirected, directed, and multigraphs.
- **Graph Algorithms**: Provides a wide range of algorithms for network analysis such as shortest path, clustering, and centrality measures.
- **Flexibility**: Allows for easy integration with other Python libraries like NumPy, SciPy, and Matplotlib.
- **Visualization**: Offers basic tools for visualizing networks.

## Installation

To install NetworkX, you can use pip:

```bash
pip install networkx
```

## Basic Usage

### Creating a Graph

You can create a simple graph and add nodes and edges as follows:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_nodes_from([2, 3])

# Add edges
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 1)])

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
```

### Analyzing a Graph

NetworkX provides various functions to analyze the properties of graphs. For example, you can calculate the shortest path between two nodes:

```python
# Shortest path between nodes 1 and 3
shortest_path = nx.shortest_path(G, source=1, target=3)
print("Shortest path:", shortest_path)
```

### Graph Algorithms

NetworkX includes many algorithms for network analysis. Here are a few examples:

#### Clustering Coefficient

The clustering coefficient measures the degree to which nodes in a graph tend to cluster together.

```python
clustering_coeff = nx.clustering(G)
print("Clustering Coefficient:", clustering_coeff)
```

#### Degree Centrality

Degree centrality is a measure of the importance of a node based on the number of connections it has.

```python
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)
```

## Advanced Features

### Directed Graphs

NetworkX supports directed graphs, which have edges with a direction.

```python
# Create a directed graph
DG = nx.DiGraph()

# Add edges with direction
DG.add_edge(1, 2)
DG.add_edge(2, 3)

# Draw the directed graph
nx.draw(DG, with_labels=True, arrows=True)
plt.show()
```

### Multigraphs

Multigraphs allow multiple edges between the same pair of nodes.

```python
# Create a multigraph
MG = nx.MultiGraph()

# Add multiple edges between nodes
MG.add_edge(1, 2)
MG.add_edge(1, 2, weight=2)

# Draw the multigraph
nx.draw(MG, with_labels=True)
plt.show()
```

### Graph Visualization

NetworkX can be integrated with Matplotlib for visualizing graphs. Here is an example of visualizing a graph with different node colors and sizes:

```python
# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Define node colors and sizes
node_colors = ['red', 'blue', 'green', 'yellow']
node_sizes = [1000, 2000, 3000, 4000]

# Draw the graph with custom node colors and sizes
nx.draw(G, with_labels=True, node_color=node_colors, node_size=node_sizes)
plt.show()
```

## Conclusion

NetworkX is a versatile and powerful library for network analysis and visualization. Its extensive range of features and ease of use make it an excellent choice for both beginners and advanced users in the field of network science.

For more detailed information and advanced usage, you can refer to the [NetworkX documentation](https://networkx.org/documentation/stable/).

---

Feel free to ask if you have any specific questions or need further examples!

Zdroj: konverzace s Copilotem, 15. 11. 2024
(1) SNAP Graph Summary — NetworkX 3.4.2 documentation. https://networkx.org/documentation/stable/auto_examples/algorithms/plot_snap.html.
(2) Summarization — NetworkX 3.4.2 documentation. https://networkx.org/documentation/stable/reference/algorithms/summarization.html.
(3) A Beginner’s Guide to NetworkX - Medium. https://medium.com/@fayam69420/a-beginners-guide-to-networkx-d959722f2d6b.
(4) Examples and Jupyter Notebooks about NetworkX - GitHub. https://github.com/networkx/nx-guides.
(5) Welcome to nx-guides! — NetworkX Notebooks. https://networkx.org/nx-guides/index.html.
(6) Network Science with Python and NetworkX Quick Start Guide. https://subscription.packtpub.com/book/data/9781789955316/1/ch01lvl1sec04/what-is-networkx.