# IR Homework 2
## Install
```
pipenv install
```
## About

### Goal
In this assignment, you will be developing the PageRank algorithm for the given graph.. 

### Input

#### Format
Graph: Your implementation can expect your graph to be submitted in adjacency matrix format, through a text file 
(call it graph.txt). This document will contain graph structure in matrix format, with three columns (i, j, k). 
Each row will denote information for a cell. e.g. a row of the form "i j k" denotes that the matrix contains a value k 
at the row i column j.  The value k=1 denotes that there is a link from document (node) i to document (node) j.

Parameters: In your implementations use beta=0.85 as the dampening factor.

#### Example

##### Graph
![alt text](https://github.com/JackKell/page-ranking-example/images/exampleGraph.png "Example Graph")

##### Adjacency Matrix File
The adjacency matrix file assumes the following:
- The first nodes is assumed to be `0`
- The last node is the largest node number provided
- Any combinations of `i` and `j` that are not provided are assumed to have a `k` of `0`
- Values are delineated by spaces
###### Format
```
i j k
i = row
j = column
k = the number of connections
```
###### Example
```
0 1 1
1 0 1
1 2 1
1 3 1
1 4 1
2 1 1
2 4 1
3 1 1
3 4 1
4 1 1
4 2 1
4 3 1
5 4 1
```

##### Connection Matrix
```
[
    [0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0]
]
```

### Output

#### Requirements
- What is the output for Matrix M? Give the matrix. 
- What is the original rank vector (rj)?
- What is the Converged rank vector (R)?
- How many  iterations did it take to get the convergence?

#### Example

