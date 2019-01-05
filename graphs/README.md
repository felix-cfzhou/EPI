# Graphs

- graphs are excellent for modeling and analyzing relationships between pairs of objects
    - list of outcomes of matches between pairs of teams
- employ graphs when the problem involves spatially connected objects
    - ie road segments between cities
- DFS is good for analyzing structures
    - ie looking for cycles or connected components
- BFS, Dijkstra's shortest path algorithm, minimum spanning trees are appropriate for optimization problems

## Graph Search

- Depth-First Search (DFS)
    - `O(|V| + |E|)` time complexity
    - `O(|V|)` space complexity
    - can check for presence of cycles
- Breadth-First Search (BFS)
    - `O(|V| + |E|)` time complexity
    - `O(|V|)` space complexity
    - can compute distance from root node
