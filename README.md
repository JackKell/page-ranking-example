# IR Homework 2
## Install Instructions
1.) Clone the project
```
git clone https://github.com/kanbei7/IR-Project.git
```
2.) Install the Python dependency manager `pipenv`
```
pip install pipenv
```
3.) Navigate to the project directory
```
cd PATH\TO\page-ranking-example
```
4.) Create the Python virtual environment and install all dependencies
```
pipenv install -d
```
5.) Add the project to your PYTHONPATH environment variable
```
set PYTHONPATH=%PYTHONPATH%;PATH\TO\page-ranking-example
```
For example,
```
set PYTHONPATH=%PYTHONPATH%;C:\Dev\IR-Project
``` 
6.) Activate the virtual environment
```
pipenv shell
```
7.) *Optional Step*: Check that the project is using the correct virtual environment
```
which python
```
8.) Run the python file of your choice
```
python path-to-file
```
9.) To close the virtual environment pipenv shell
```
exit
```
## Running the Project
After following the install instructions simply run the project doing the following:
```
python irhw2 PATH\TO\given\graph
```
For example in this project you can run a couple of graphs that I have already provided such as:
```
python irhw2 data/graph.txt
```
## About

### Goal
This project implements the random surfer page ranking algorithm for any given graph text file. 

### Input

#### Format
Graph: Your implementation can expect your graph to be submitted in adjacency matrix format, through a text file 
(call it graph.txt). This document will contain graph structure in matrix format, with three columns (i, j, k). 
Each row will denote information for a cell. e.g. a row of the form "i j k" denotes that the matrix contains a value k 
at the row i column j.  The value k=1 denotes that there is a link from document (node) i to document (node) j.

Parameters: In your implementations use beta=0.85 as the dampening factor.

#### Example

##### Graph
![alt text](https://github.com/JackKell/page-ranking-example/blob/master/images/exampleGraph.png "Example Graph")

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
1 2 1
1 3 1
1 4 1
2 1 1
2 3 1
2 4 1
3 1 1
3 2 1
3 4 1
4 1 1
4 2 1
4 3 1
4 5 1
```

##### Connection Matrix
```
[[ 0.  0.  0.  0.  0.  0.]
 [ 1.  0.  1.  1.  1.  0.]
 [ 0.  1.  0.  1.  1.  0.]
 [ 0.  1.  1.  0.  1.  0.]
 [ 0.  1.  1.  1.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.]]
```

### Output
#### Project Requirements
- What is the output for Matrix M? Give the matrix. 
- What is the original rank vector (rj)?
- What is the Converged rank vector (R)?
- How many  iterations did it take to get the convergence?

#### Example
```
Connection Matrix
[[ 0.  0.  0.  0.  0.  0.]
 [ 1.  0.  1.  1.  1.  0.]
 [ 0.  1.  0.  1.  1.  0.]
 [ 0.  1.  1.  0.  1.  0.]
 [ 0.  1.  1.  1.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.]]
Transition Matrix M:
[[ 0.          0.          0.          0.          0.          0.        ]
 [ 1.          0.          0.33333333  0.33333333  0.25        0.        ]
 [ 0.          0.33333333  0.          0.33333333  0.25        0.        ]
 [ 0.          0.33333333  0.33333333  0.          0.25        0.        ]
 [ 0.          0.33333333  0.33333333  0.33333333  0.          0.        ]
 [ 0.          0.          0.          0.          0.25        0.        ]]
Ranking at Iteration 0:
[ 0.16666667  0.16666667  0.16666667  0.16666667  0.16666667  0.16666667]
Converge Ranking at Iteration 12 :
[ 0.025    0.16261  0.14605  0.14605  0.15463  0.05807]
Total Iterations to reach convergence: 12
```
