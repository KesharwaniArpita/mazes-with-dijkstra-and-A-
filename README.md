<h1>Maze Solving with Dijkstra and A* Algorithm</h1>
This project contains the algorithm implementation for path finding in a maze using Dijkstra and A* algorithm. We have also compared the time effieciency and  space efficiency of both the algorithms.

<h2>Contributers</h2>
1. <a href = "https://github.com/Abhishek02bhardwaj/">Abhishek Bhardwaj</a><br>
2. <a href = "https://github.com/KesharwaniArpita">Arpita Kesharwani</a>

<h2>Maze</h2>
1)The mazes are constructed using the pyamaze module in python.<br>
2)Then one single maze is solved using A* algorithm , first , then the Dijkstra algorithm is used.<br>

<h2>A* Algorithm</h2>
1)A* algorithm is heuristic search algorithm as it uses the heuristic function h(n).<br>
2)A heuristic function, also simply called a heuristic, is a function that ranks alternatives in search algorithms at each branching step based on available information to decide which branch to follow.<br>
3)It searches for shorter paths first rather than the longer paths.<br>
4)It uses an evaluation to guide the selection of node. F(n) = g(n) + h(n).<br>
5)In this formula, g (n) represents the weight of the path from the starting point to node n and h (n) is the heuristic weight while f (n) is estimated cost of path from node n to target node.<br>

<h2>Dijkstra Algorithm</h2>
1)Dijkstra algorithm is a single-source shortest path algorithm.<br>
2)Single-source means that only one source is given, and we have to find the shortest path from the source to all the nodes.<br>
3)It is a type of greedy algorithm (which means it picks the best immediate output, but does not consider the big picture).<br>
4)It only works on weighted graph with positive weights.<br>
