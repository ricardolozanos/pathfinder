******************Introduction******************
PathFind is a command-line and GUI-based application for finding paths on maps using various algorithms. 
It comes with two executable options: one with a graphical user interface (GUI) and another without GUI. 
This README provides information on how to use both versions of the application.

***Quick-Intro***

For no Gui:
PathFind-No-Gui.lnk map{i}.txt {algorithm}
"i" is a number currently from 1-13
algorithm - ids or IDS / bfs or BFS / a,A,a* or A*
ex: PathFind-No-Gui.lnk map1.txt a*

For Gui:
PathFind.lnk


Table of Contents
-Getting Started
-Prerequisites
-Installation
-Usage
-PathFind with GUI
-PathFind without GUI
-Map Files
-Algorithms
-Contributions

******************Getting Started******************

******************Installation******************

Clone this repository to your local machine:

- git clone https://github.com/ricardolozanos/pathfinder

******************Usage******************

****PathFind with GUI****
To run the PathFind GUI, navigate to the project's root directory and execute the following command:

PathFind-Gui.lnk

You can also navigate to the "Gui" folder and run the same command to launch the GUI.

Once the GUI is open, you can select a map from the "Gui/map/" folder which are shown on the left-top side, 
choose an algorithm from the dropdown menu on the left-bottom, and 
click the "Run" button to execute the PathFind script. 

The results will be displayed at the bottom of the GUI.

****PathFind without GUI****
To run the PathFind without GUI, navigate to the project's root directory and execute the following command:

PathFind-No-Gui.lnk map{i}.txt {algorithm}

Replace {i} with the map number (e.g., 1, 2, 3, ...).
 The {algorithm} parameter can be one of the following options: ids, bfs, a (or A),
 which correspond to different pathfinding algorithms.
 The case of the algorithm name is not significant.

****Map Files****

The map files are stored in the "Gui/map/" and "NoGui/map/" folders. 
These files must be named "map{i}.txt," where {i} is a number ranging from 1 to 13.

You can select these maps when using either the GUI or the command-line version.

****Algorithms****
PathFind supports multiple pathfinding algorithms, including:

ids or IDS		(Iterative Deepening Search)
bfs or BFS		(Breadth-First Search)
a , A , a* or A* 	(A* Search)

You can choose one of these algorithms when running the PathFind without GUI.

Contributions:

-Ricardo Lozano

-Ivan Montoya


***** Test Cases *****


********Map1.txt
5 5
4 2
0 1
1 1 0 5 3
2 1 1 4 0
0 3 3 4 4
1 1 3 0 2
5 2 3 3 4

Breadth-First Search (BFS):

Path: [(4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]
Path Cost: 8
Nodes Expanded: 18
Maximum Nodes Held in Memory: 19
Total Run Time (ms): 0.0

Iterative Deepening Search (IDS):

Path: [(4, 2), (3, 2), (2, 2), (1, 2), (1, 1), (0, 1)]
Path Cost: 9
Nodes Expanded: 6
Maximum Nodes Held in Memory: 13
Total Run Time (ms): 0.0

A Search (A):**

Path: [(4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]
Path Cost: 8
Nodes Expanded: 16
Maximum Nodes Held in Memory: 23
Total Run Time (ms): 0.0

Reflection, Map1:

-All three algorithms (BFS, IDS, A*) found a valid path from the starting location (4, 2) to the goal location (0, 1).
-The BFS and A* algorithms both found a path with a path cost of 8, while IDS found a path with a slightly higher cost of 9.
-The number of nodes expanded and the maximum nodes held in memory varied between the algorithms,
 with BFS expanding the most nodes and IDS expanding the fewest.
-The runtime for all three algorithms on this small map was very fast (0.0 ms).


********Map2.txt
10 10
9 8
5 2
5 0 2 0 3 1 3 1 0 1
3 1 5 3 5 4 4 2 2 0
5 3 4 4 2 1 2 0 4 4
2 2 0 2 4 0 2 3 0 2
1 3 5 4 0 1 4 2 5 2
2 5 4 1 1 5 1 2 1 3
0 2 0 1 1 0 1 3 3 3
3 3 2 4 4 3 4 3 5 5
1 3 4 5 3 0 1 0 4 5
2 3 0 1 5 5 1 1 4 2


Breadth-First Search (BFS):

Path: [(9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (5, 2)]
Path Cost: 28
Nodes Expanded: 54
Maximum Nodes Held in Memory: 58
Total Run Time (ms): 0.0

Iterative Deepening Search (IDS):

Path: [(9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (5, 3), (5, 2)]
Path Cost: 26
Nodes Expanded: 55
Maximum Nodes Held in Memory: 40
Total Run Time (ms): 0.0

A Search (A):

Path: [(9, 8), (9, 7), (9, 6), (8, 6), (7, 6), (6, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2)]
Path Cost: 20
Nodes Expanded: 61
Maximum Nodes Held in Memory: 66
Total Run Time (ms): 0.0

Reflection, Map2:

-All three algorithms (BFS, IDS, A*) found a valid path from the starting location (9, 8) to the goal location (5, 2).
-A* with the Manhattan distance heuristic found the most efficient path with a cost of 20.
-The number of nodes expanded and the maximum nodes held in memory were different for each algorithm,
 with A* expanding the most nodes but finding the optimal path.
-The runtime for all three algorithms on this map was very fast (0.0 ms).
-In this case, A* with the heuristic provided the most efficient solution.


********Map3.txt
15 15
14 0
0 14
0 3 3 3 1 2 2 5 5 0 4 1 4 0 2
1 3 4 1 3 0 3 3 1 3 0 4 3 3 3
3 4 4 5 0 5 0 4 2 3 1 3 5 2 2
4 2 0 1 1 2 1 5 2 3 2 3 1 0 1
0 5 4 2 4 5 4 2 4 1 5 5 5 2 0
5 4 4 5 5 4 0 3 5 5 4 4 1 1 5
5 4 5 3 3 0 1 2 3 0 5 2 0 2 1
2 1 3 5 4 2 3 1 0 3 4 5 5 3 2
1 2 5 4 5 0 1 5 2 0 1 0 1 0 4
5 5 4 2 5 2 5 3 1 3 2 1 3 4 1
2 3 1 0 1 0 1 1 1 1 5 3 5 1 4
4 4 3 1 1 3 5 5 5 3 0 5 0 1 5
1 5 2 0 1 2 3 1 4 3 3 5 2 0 1
2 3 1 3 5 2 2 2 5 3 5 2 3 1 1
2 2 3 3 0 2 1 2 2 1 1 1 2 5 0

Breadth-First Search (BFS):

Path: [(14, 0), (14, 1), (14, 2), (14, 3), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7),
	 (13, 8), (13, 9), (12, 9), (11, 9), (10, 9), (10, 10), (9, 10), (8, 10),
	 (7, 10), (7, 11), (6, 11), (5, 11), (5, 12), (4, 12), (3, 12), (2, 12),
	 (2, 13), (2, 14), (1, 14), (0, 14)]
Path Cost: 81
Nodes Expanded: 197
Maximum Nodes Held in Memory: 196
Total Run Time (ms): 1.3782978057861328

Iterative Deepening Search (IDS):

Path: [(14, 0), (13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (7, 0), (6, 0), (5, 0),
 	(5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (1, 3),
 	(0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (1, 7), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8),
 	(4, 8), (5, 8), (5, 9), (4, 9), (3, 9), (2, 9), (2, 10), (2, 11), (1, 11), (0, 11),
 	(0, 12), (1, 12), (1, 13), (1, 14), (0, 14)]
Path Cost: 139
Nodes Expanded: 237
Maximum Nodes Held in Memory: 183
Total Run Time (ms): 49.90816116333008

A Search (A):

Path: [(14, 0), (13, 0), (13, 1), (13, 2), (12, 2), (11, 2), (11, 3), (11, 4), (10, 4), (9, 4),
	 (9, 5), (9, 6), (8, 6), (7, 6), (6, 6), (6, 7), (5, 7), (4, 7), (4, 8), (4, 9), (3, 9),
	 (3, 10), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (1, 14), (0, 14)]
Path Cost: 66
Nodes Expanded: 2229
Maximum Nodes Held in Memory: 438
Total Run Time (ms): 7.083415985107422

Reflection, Map3:

-All three algorithms found a valid path from the starting location (14, 0) to the goal location (0, 14).

-BFS found a path with a cost of 81,
 requiring 197 node expansions and a maximum of 196 nodes held in memory.
 The runtime was relatively fast at 1.378 milliseconds.


IDS found a path with a cost of 139,
 expanding 237 nodes and holding a maximum of 183 nodes in memory.
 IDS took significantly longer than BFS, with a runtime of 49.908 milliseconds.

A* found a more efficient path with a cost of 66,
 but it expanded a much larger number of nodes (2229) compared to BFS and IDS.
 A* held a maximum of 438 nodes in memory, and the runtime was 7.083 milliseconds.

In this case, A* found the most efficient path in terms of cost,
 but it required significantly more node expansions and memory compared to BFS and IDS.
 The choice of algorithm may depend on the trade-off between computational resources and finding the optimal path.


********Map4.txt
20 20
16 4
3 18
2 3 4 1 3 1 5 1 3 0 1 0 4 4 4 5 0 1 1 0
1 4 2 5 3 3 4 0 5 5 3 1 3 5 4 4 5 3 4 5
3 4 2 3 1 5 1 2 4 0 2 0 4 3 2 2 3 1 3 5
2 0 2 0 1 3 3 0 2 5 1 2 5 1 2 1 1 5 5 4
4 5 5 5 3 5 3 3 1 0 4 3 0 1 4 1 0 1 2 3
2 4 4 2 0 4 5 0 1 2 3 4 2 2 3 4 2 3 5 4
1 1 3 0 5 2 5 5 5 2 1 5 5 3 0 5 5 5 0 3
3 0 4 2 0 2 0 1 0 1 2 0 1 4 1 2 0 4 5 4
0 4 4 5 1 5 1 5 1 1 2 5 0 3 3 4 1 5 5 0
1 5 5 5 0 1 0 3 0 4 2 0 1 3 4 1 3 0 2 3
1 0 1 1 1 5 4 5 5 1 0 1 0 1 5 3 0 2 0 3
5 3 4 5 1 4 3 3 4 2 1 1 1 5 2 4 3 3 1 4
1 1 1 4 4 1 1 5 0 1 0 3 1 4 1 1 1 3 5 3
4 0 3 1 4 0 3 5 1 0 3 2 2 5 5 3 5 0 1 3
2 4 5 1 3 2 4 4 4 2 1 2 3 0 3 2 3 4 5 0
5 1 1 2 1 3 5 5 0 1 0 1 2 1 1 3 5 0 1 1
4 5 4 0 4 1 3 3 2 1 1 4 5 2 4 4 4 4 3 4
5 0 5 1 3 0 1 2 5 2 5 0 3 1 3 1 4 2 1 2
3 1 5 1 2 1 2 0 4 4 5 2 5 4 5 5 2 2 5 5
5 2 0 4 1 1 3 2 2 1 1 5 1 3 4 4 5 5 2 5

Breadth-First Search (BFS):

Path: [(16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11),
	 (16, 12), (16, 13), (16, 14), (16, 15), (15, 15), (14, 15), (13, 15),
	 (12, 15), (11, 15), (10, 15), (9, 15), (9, 16), (8, 16), (8, 17), (7, 17),
	 (6, 17), (5, 17), (5, 18), (4, 18), (3, 18)]
Path Cost: 80
Nodes Expanded: 335
Maximum Nodes Held in Memory: 338
Total Run Time (ms): 1.2969970703125

Iterative Deepening Search (IDS):

Path: [(16, 4), (15, 4), (14, 4), (13, 4), (12, 4), (11, 4), (10, 4), (10, 5),
	 (10, 6), (10, 7), (9, 7), (8, 7), (8, 8), (8, 9), (7, 9), (6, 9),
	 (5, 9), (5, 10), (4, 10), (3, 10), (2, 10), (1, 10), (1, 11), (1, 12),
	 (0, 12), (0, 13), (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (5, 14),
	 (4, 14), (3, 14), (2, 14), (2, 15), (2, 16), (2, 17), (3, 17), (3, 18)]
Path Cost: 107
Nodes Expanded: 373
Maximum Nodes Held in Memory: 267
Total Run Time (ms): 49.62801933288574

A Search (A):*

Path: [(16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (15, 9), (14, 9),
	 (14, 10), (14, 11), (13, 11), (13, 12), (12, 12), (11, 12), (11, 13),
	 (10, 13), (9, 13), (8, 13), (7, 13), (6, 13), (5, 13), (4, 13), (3, 13),
	 (3, 14), (3, 15), (3, 16), (3, 17), (3, 18)]
Path Cost: 59
Nodes Expanded: 1043
Maximum Nodes Held in Memory: 388
Total Run Time (ms): 0.0


Reflection, Map4:

All three algorithms (BFS, IDS, A*) found valid paths from the starting location (16, 4) to the goal location (3, 18).
However, A*  found the most efficient path with a cost of 59.
The number of nodes expanded and the maximum nodes held in memory were different for each algorithm,
 with A* expanding the most nodes but finding the optimal path.
The runtime for BFS and A* was relatively fast,
 while IDS took significantly more time due to its iterative nature.

***********Map5.txt
25 25
21 22
22 7
3 5 1 2 5 4 4 4 1 3 4 1 5 3 3 1 2 0 1 4 3 4 2 0 4
0 5 5 2 2 4 1 5 5 0 2 4 0 2 3 2 4 2 0 2 3 2 1 4 5
4 4 0 4 1 3 4 1 3 3 3 0 1 0 1 3 2 2 2 1 2 1 2 2 1
1 5 1 4 3 1 5 1 4 0 1 5 2 5 5 2 4 5 1 5 1 2 2 1 5
3 2 5 1 5 1 0 1 2 3 0 2 0 5 3 2 1 2 4 5 4 5 0 4 0
0 2 4 1 4 5 1 2 3 2 4 0 5 2 2 3 0 1 5 3 1 1 3 3 5
4 4 5 5 4 3 0 5 4 0 1 4 5 1 4 0 3 4 2 4 0 1 3 4 3
4 5 4 2 5 3 1 4 3 1 3 2 1 1 5 2 3 0 3 1 4 3 2 3 1
3 5 0 1 5 1 1 5 3 1 3 4 2 3 5 4 1 2 0 3 1 3 2 1 3
4 1 3 0 2 4 4 0 1 0 5 0 2 4 2 3 5 1 2 2 0 4 2 2 0
4 2 5 3 3 0 1 3 2 2 0 2 0 5 2 5 4 1 5 3 5 0 4 0 5
1 3 4 0 4 1 2 4 3 4 4 1 1 1 3 5 3 2 5 5 1 1 3 3 0
1 2 3 1 0 3 3 0 4 3 5 0 3 4 2 3 5 1 3 5 1 0 4 0 5
1 2 5 2 2 3 3 4 2 2 5 4 3 2 4 1 3 2 2 0 2 1 1 1 1
3 3 1 2 1 3 2 1 5 3 1 4 1 4 3 1 4 4 1 3 1 4 5 2 2
0 1 0 5 5 2 1 0 5 1 2 3 0 4 3 0 3 5 5 3 5 0 2 0 5
4 0 5 2 0 4 4 1 2 0 3 1 1 1 3 3 0 1 3 2 1 3 3 3 3
2 5 4 0 1 1 2 1 1 1 1 4 0 3 4 0 1 4 0 1 0 3 4 3 3
0 1 2 3 5 2 2 1 0 5 0 4 4 0 2 1 3 2 3 5 3 4 5 2 1
2 5 1 1 1 2 4 3 2 4 3 5 5 5 2 0 1 2 3 0 1 3 3 5 0
2 1 5 5 3 3 0 2 2 4 3 4 5 5 5 5 3 4 5 1 3 3 5 4 5
5 4 4 0 1 3 1 5 2 4 4 4 3 2 4 4 1 5 0 1 5 3 3 4 3
4 0 2 2 4 1 2 3 2 3 0 1 3 2 1 1 4 2 3 0 4 0 3 0 1
4 2 2 5 0 5 3 1 4 5 1 5 1 1 0 5 3 5 2 4 5 2 3 1 2
5 3 4 1 1 2 4 0 1 5 0 4 3 4 1 5 0 2 1 5 5 4 3 2 1

Breadth-First Search (BFS):

Path: [(21, 22), (21, 21), (21, 20), (21, 19), (20, 19), (20, 18), (20, 17),
 (20, 16), (20, 15), (20, 14), (20, 13), (20, 12), (20, 11), (20, 10),
 (20, 9), (20, 8), (20, 7), (21, 7), (22, 7)]
Path Cost: 65
Nodes Expanded: 216
Maximum Nodes Held in Memory: 236
Total Run Time (ms): 0.0

Iterative Deepening Search (IDS):

Path: [(21, 22), (20, 22), (19, 22), (18, 22), (17, 22), (16, 22), (16, 21),
 (16, 20), (15, 20), (15, 19), (14, 19), (14, 18), (13, 18), (13, 17), (14, 17),
 (15, 17), (16, 17), (17, 17), (18, 17), (18, 16), (19, 16), (20, 16), (21, 16),
 (22, 16), (23, 16), (23, 15), (24, 15), (24, 14), (24, 13), (24, 12), (24, 11),
 (23, 11), (23, 10), (23, 9), (22, 9), (22, 8), (22, 7)]
Path Cost: 112
Nodes Expanded: 400
Maximum Nodes Held in Memory: 273
Total Run Time (ms): 50.040483474731445

A Search (A):

Path: [(21, 22), (21, 21), (20, 21), (20, 20), (20, 19), (20, 18), (20, 17),
 (20, 16), (21, 16), (21, 15), (22, 15), (22, 14), (22, 13), (23, 13), (23, 12),
 (23, 11), (23, 10), (23, 9), (22, 9), (22, 8), (22, 7)]
Path Cost: 52
Nodes Expanded: 1391
Maximum Nodes Held in Memory: 704
Total Run Time (ms): 4.999399185180664

Reflection, Map5:

All three algorithms found a valid path from the starting location (21, 22) to the goal location (22, 7).

BFS found a path with a cost of 65, requiring 216 node expansions and a maximum of 236 nodes held in memory.
 The runtime was relatively fast, at 0.0 milliseconds.

IDS found a path with a cost of 112, expanding 400 nodes and holding a maximum of 273 nodes in memory.
 IDS took significantly longer than BFS, with a runtime of 50.040 milliseconds.

A* found a more efficient path with a cost of 52 but expanded a much larger number of nodes (1391) compared to BFS and IDS.
 A* held a maximum of 704 nodes in memory, and the runtime was 4.999 milliseconds.

In this case, A* found the most efficient path in terms of cost,
 but it required significantly more node expansions and memory compared to BFS and IDS.
 The choice of algorithm may depend on the trade-off between computational resources and finding the optimal path.
 If computational resources are not a constraint, A* can find the shortest path,
 but if efficiency and faster execution are required, BFS or IDS may be preferable.


****************************No Path available maps...
Map6.txt
10 10
0 0
2 9
5 0 2 0 3 1 3 1 0 1
3 1 5 3 5 4 4 2 2 0
5 3 4 4 2 1 2 0 0 4
2 2 0 2 4 0 2 3 0 2
1 3 5 4 0 1 4 2 5 0
2 5 4 1 1 5 1 2 1 3
0 2 0 1 1 0 1 3 3 3
3 3 2 4 4 3 4 3 5 5
1 3 4 5 3 0 1 0 4 5
2 3 0 1 5 5 1 1 4 2

Breadth-First Search (BFS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 80
Max Nodes: 79
Total Run time (ms): 0.9243488311767578

Iterative Deepening Search (IDS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 121
Max Nodes: 107
Total Run time (ms): 331.29310607910156

A Search (A):*

The path followed was: []
The path cost was: -1
Nodes Expanded: 422
Max Nodes: 137
Total Run time (ms): 0.0

Reflection Map6.

None of the three algorithms (BFS, IDS, A*) were able to find a valid path from the starting location 
(0, 0) to the goal location (2, 9).

BFS, IDS, and A* all returned empty paths with a path cost of -1,
 indicating that there is no valid path between the given start and goal points.

BFS expanded 80 nodes, IDS expanded 121 nodes, and A* expanded 422 nodes in an attempt to find a path.

BFS held a maximum of 79 nodes in memory and had a runtime of 0.924 milliseconds.
 IDS held a maximum of 107 nodes in memory and took significantly longer with a runtime of 331.293 milliseconds.
 A* expanded the most nodes (422) but had a faster runtime of 0.0 milliseconds.

**************Map7.txt
20 20
16 4
0 0
2 0 4 1 3 1 5 1 3 0 1 0 4 4 4 5 0 1 1 0
0 4 2 5 3 3 4 0 5 5 3 1 3 5 4 4 5 3 4 5
3 4 2 3 1 5 1 2 4 0 2 0 4 3 2 2 3 1 3 5
2 0 2 0 1 3 3 0 2 5 1 2 5 1 2 1 1 5 5 4
4 5 5 5 3 5 3 3 1 0 4 3 0 1 4 1 0 1 2 3
2 4 4 2 0 4 5 0 1 2 3 4 2 2 3 4 2 3 5 4
1 1 3 0 5 2 5 5 5 2 1 5 5 3 0 5 5 5 0 3
3 0 4 2 0 2 0 1 0 1 2 0 1 4 1 2 0 4 5 4
0 4 4 5 1 5 1 5 1 1 2 5 0 3 3 4 1 5 5 0
1 5 5 5 0 1 0 3 0 4 2 0 1 3 4 1 3 0 2 3
1 0 1 1 1 5 4 5 5 1 0 1 0 1 5 3 0 2 0 3
5 3 4 5 1 4 3 3 4 2 1 1 1 5 2 4 3 3 1 4
1 1 1 4 4 1 1 5 0 1 0 3 1 4 1 1 1 3 5 3
4 0 3 1 4 0 3 5 1 0 3 2 2 5 5 3 5 0 1 3
2 4 5 1 3 2 4 4 4 2 1 2 3 0 3 2 3 4 5 0
5 1 1 2 1 3 5 5 0 1 0 1 2 1 1 3 5 0 1 1
4 5 4 0 4 1 3 3 2 1 1 4 5 2 4 4 4 4 3 4
5 0 5 1 3 0 1 2 5 2 5 0 3 1 3 1 4 2 1 2
3 1 5 1 2 1 2 0 4 4 5 2 5 4 5 5 2 2 5 5
5 2 0 4 1 1 3 2 2 1 1 5 1 3 4 4 5 5 2 5


Breadth-First Search (BFS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 343
Max Nodes: 342
Total Run time (ms): 0.0

Iterative Deepening Search (IDS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 548
Max Nodes: 493
Total Run time (ms): 1449.476957321167

A* Search (A*):

The path followed was: []
The path cost was: -1
Nodes Expanded: 1120
Max Nodes: 390
Total Run time (ms): 4.068851470947266

Reflection, Map7:

None of the three algorithms (BFS, IDS, A*) were able to find a valid path from the starting location
 (0, 0) to the goal location (2, 9).

All three algorithms returned empty paths with a path cost of -1,
 indicating that there is no valid path between the given start and goal points.

BFS expanded 343 nodes, IDS expanded 548 nodes, and A* expanded 1120 nodes in an attempt to find a path.

BFS held a maximum of 342 nodes in memory and had a runtime of 0.0 milliseconds. 
IDS held a maximum of 493 nodes in memory and took significantly longer with a runtime of 1449.476 milliseconds. 
A* expanded the most nodes (1120) but had a runtime of 4.068 milliseconds.

In this case, none of the algorithms were able to find a path, and A* was the fastest among them in terms of runtime.

**************Map8.txt
30 30
0 0
6 22
2 1 4 0 5 1 0 1 4 5 0 1 0 1 2 1 0 3 5 4 1 4 0 2 5 3 4 5 0 4
1 5 3 0 2 0 1 1 4 2 5 5 1 0 5 4 4 2 3 2 1 0 5 2 2 3 2 4 2 3
0 0 0 4 2 3 1 4 5 0 1 5 4 1 0 1 3 2 1 2 4 4 5 5 2 4 1 5 2 0
2 4 4 1 5 5 4 0 2 1 3 5 0 1 1 2 3 5 3 2 0 5 5 0 3 4 4 5 5 3
5 0 3 4 1 3 2 1 2 5 2 1 5 1 5 3 4 5 4 2 2 4 2 1 5 1 0 1 2 4
2 5 1 1 3 2 0 2 1 3 1 0 5 4 1 0 5 4 1 1 4 0 5 0 4 0 2 0 2 1
2 1 0 1 0 1 4 2 2 3 3 4 3 4 5 3 3 1 1 5 0 2 4 5 1 1 3 4 0 5
4 4 1 2 5 3 0 2 3 5 4 5 0 1 5 5 3 1 5 5 3 1 1 4 4 3 0 1 1 5
4 4 2 2 4 0 2 1 5 1 1 0 2 4 2 4 2 1 4 1 0 1 2 0 3 0 5 0 5 5
2 2 5 3 3 3 4 5 1 2 0 3 1 2 1 5 3 2 2 3 5 2 0 2 3 1 0 1 2 1
3 4 5 3 5 3 4 3 4 2 3 4 5 4 1 3 3 0 5 0 3 2 5 2 2 0 1 3 5 2
2 1 0 1 4 5 0 3 2 4 5 2 4 5 0 5 1 1 5 1 5 3 0 4 0 5 1 1 1 4
4 1 3 0 5 0 3 2 0 5 0 4 0 1 5 2 1 0 1 2 3 3 3 5 1 2 4 4 5 2
2 0 4 1 4 1 3 5 1 5 5 1 5 3 3 4 0 3 0 5 5 0 2 2 3 5 5 2 4 4
0 1 4 1 0 1 5 1 1 1 0 1 5 0 4 3 1 0 2 1 5 5 0 1 3 1 2 3 1 3
5 2 3 2 2 3 3 3 2 4 1 1 4 1 2 1 3 1 2 2 3 2 3 3 1 2 4 0 5 1
3 5 0 3 0 1 1 0 3 2 0 1 5 3 4 3 4 0 5 3 5 5 1 3 0 4 5 2 1 3
3 0 3 1 2 0 5 2 2 1 2 4 5 1 0 3 4 1 0 1 5 2 1 1 1 2 3 3 0 5
5 1 1 5 5 1 3 1 0 5 3 5 3 5 3 3 0 1 4 0 5 0 5 5 1 5 5 0 1 1
2 2 2 3 1 5 0 1 4 5 5 5 0 4 5 3 2 4 4 3 5 4 5 5 5 3 3 5 0 1
4 3 3 1 5 1 4 0 1 5 5 5 3 2 0 1 1 2 0 5 5 4 3 2 5 5 2 4 1 4
4 1 1 1 5 3 0 3 3 2 3 4 4 4 5 0 3 2 2 5 5 4 1 1 5 3 3 4 1 3
3 0 1 1 4 2 5 3 2 2 4 2 2 3 1 5 4 1 4 0 1 5 2 4 0 3 2 5 5 3
4 1 3 0 2 4 4 0 5 3 5 4 1 4 4 5 3 4 4 5 1 1 3 5 5 1 2 3 4 4
2 2 0 1 2 0 1 5 2 2 5 3 5 4 3 4 3 5 1 0 3 5 3 1 1 5 3 2 5 5
2 5 1 2 4 5 3 2 1 1 0 2 3 1 1 4 3 5 1 2 0 2 0 4 1 3 1 0 1 1
2 3 1 3 4 2 0 4 1 5 4 3 4 3 5 1 3 4 3 5 4 0 4 1 4 1 0 3 1 3
2 5 2 4 4 2 3 1 0 2 2 1 4 0 2 5 5 3 1 1 4 1 0 5 1 4 1 2 1 0
0 1 0 2 3 1 2 5 2 3 5 5 0 1 4 2 0 3 4 2 2 3 1 4 0 5 1 4 5 5
1 0 3 1 0 1 0 1 0 1 3 0 1 3 1 5 2 2 1 0 1 1 1 5 1 4 0 1 0 2

Breadth-First Search (BFS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 6
Max Nodes: 5
Total Run time (ms): 0.0

Iterative Deepening Search (IDS):

The path followed was: []
The path cost was: -1
Nodes Expanded: 8
Max Nodes: 7
Total Run time (ms): 20.074844360351562

A* Search (A*):

The path followed was: []
The path cost was: -1
Nodes Expanded: 9
Max Nodes: 8
Total Run time (ms): 0.0

Reflection, Map8:

None of the three algorithms (BFS, IDS, A*) were able to find a valid path from the starting location 
(0, 0) to the goal location (6, 22).

All three algorithms returned empty paths with a path cost of -1,
 indicating that there is no valid path between the given start and goal points.

BFS expanded 6 nodes, IDS expanded 8 nodes, and A* expanded 9 nodes in an attempt to find a path.

BFS held a maximum of 5 nodes in memory and had a runtime of 0.0 milliseconds. 
IDS held a maximum of 7 nodes in memory and took 20.074 milliseconds to run. 
A* also held a maximum of 8 nodes in memory and had a runtime of 0.0 milliseconds.

In this case, none of the algorithms were able to find a path,
 and BFS was the most efficient in terms of both runtime and memory usage.





