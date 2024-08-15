# Graph Algorithms Project

This project implements and visualizes several graph algorithms, including clustering coefficient, degree distribution, and diameter calculations. It's designed to work efficiently with large graphs using optimizations such as graph-degeneracy.

## Features

- Clustering coefficient algorithm
- Degree distribution algorithm
- Diameter algorithm
- Graph-degeneracy optimization for improved performance
- Visualization of results using matplotlib
- Support for Erdős-Rényi and Barabási-Albert graph models

You can modify the parameters in `config.py` to adjust graph sizes, types, and algorithm settings.

## Algorithms

### Clustering Coefficient

Calculates the clustering coefficient for each node in the graph, which measures the degree to which nodes tend to cluster together. The equation is 3 * number-of-triangles / number-of-2-edge-paths. A graph degeneracy is implemented to improve the efficiency of calculating the number of triangles.

### Degree Distribution

Computes the degree distribution of the graph, showing the number of nodes with each degree value.

### Diameter

Finds the maximum shortest path length between any two nodes in the graph, using an heuristic of randomly selecting a node and performing a BFS and then re-selecting the farthest node; this is computed n number of time to get a very close approximation to the actual diameter.

## Visualization

Results are plotted using matplotlib, providing visual representations of:

- Clustering coefficient distribution
- Degree distribution
- Diameter calculation results

Comparisons between Erdős-Rényi and Barabási-Albert graph models are also visualized.

## Analysis

![analysis]("analysis.png")

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
