# mazes-with-dijkstra-and-A-star
This project contains path finding in a maze using Dijkstra and A* algorithm.

## Maze: 
#### 1)The mazes are constructed using the pyamaze module in python. 
#### 2)Then one single maze is solved using A* algorithm , first , then the Dijkstra algorithm is used.

## A*: 
#### 1)A* algorithm is heuristic search algorithm as it uses the heuristic function h(n). 
#### 2)A heuristic function, also simply called a heuristic, is a function that ranks alternatives in search algorithms at each branching step based on available information to decide which branch to follow.
#### 3)It searches for shorter paths first rather than the longer paths.
#### 4)It uses an evaluation to guide the selection of node. F(n) = g(n) + h(n).
#### 5)In this formula, g (n) represents the weight of the path from the starting point to node n and h (n) is the heuristic weight while f (n) is estimated cost of path from node n to target node.

## Dijkstra:
#### 1)Dijkstra algorithm is a single-source shortest path algorithm. 
#### 2)Single-source means that only one source is given, and we have to find the shortest path from the source to all the nodes.
#### 3)It is a type of greedy algorithm (which means it picks the best immediate output, but does not consider the big picture).
#### 4)It only works on weighted graph with positive weights.
