******************Introduction******************
PathFind is a command-line and GUI-based application for finding paths on maps using various algorithms. 
It comes with two executable options: one with a graphical user interface (GUI) and another without GUI. 
This README provides information on how to use both versions of the application.

***Quick-Intro***

For no Gui:
PathFind-No-Gui.lnk map{i}.txt {algorithm}

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

- git clone https://github.com/yourusername/pathfind.git

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