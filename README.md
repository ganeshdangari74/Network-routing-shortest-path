# Network Routing & Shortest Path Simulation

A Python-based simulation of network routing using **Dijkstra’s Shortest Path Algorithm**. This project demonstrates how routing decisions are made in a communication network by computing the minimum cost paths between nodes.

---

## Overview

Routing is a fundamental concept in computer networks, where data packets must travel through a network using the most efficient path. This project models a network as a **weighted graph** and applies Dijkstra’s algorithm to determine the shortest path cost from a source node to all other nodes.

---

## Algorithm Used

* **Dijkstra’s Shortest Path Algorithm**

The algorithm iteratively selects the unvisited node with the smallest known distance and updates the distance of its neighboring nodes.

---

## Key Features

* Models a network using a weighted adjacency graph
* Computes shortest path costs from a given source node
* Demonstrates routing behavior used in real-world networks
* Simple, readable Python implementation

---

## Technologies Used

* **Programming Language:** Python 3
* **Core Concepts:** Computer Networks, Graph Algorithms, Routing

---

## Project Structure

```
network-routing-shortest-path/
│
├── routing.py    # Dijkstra’s algorithm implementation
└── README.md     # Project documentation
```

---

## How to Run the Project

1. Clone the repository or download the source code
2. Navigate to the project directory
3. Run the program using:

```bash
python routing.py
```

---

## Example Network Graph

The network is represented as a weighted graph:

```python
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2, 'E': 1},
    'E': {'D': 1}
}
```

---

## Output

The program prints the shortest path cost from the source node to all other nodes in the network.

Example:

```
Shortest path cost from A to D: 5
```

---

## Limitations

* Computes only shortest path **costs**, not the actual paths
* Does not support negative edge weights
* Static graph (no dynamic updates)

---

## Future Enhancements

* Display actual shortest paths
* Support dynamic or larger networks
* Add visualization of network topology
* Extend to other routing algorithms (Bellman-Ford, A*)

---

## Academic Relevance

This project demonstrates practical understanding of:

* Network routing principles
* Graph-based optimization algorithms
* Dijkstra’s algorithm used in routing protocols

It is suitable for **Computer Networks coursework**, **algorithm practice**, and **internship portfolios**.

---

## License

This project is open-source and intended for educational and academic use.

---

## Author

**Ganesh Dangari**
 ( Computer Science Student )
