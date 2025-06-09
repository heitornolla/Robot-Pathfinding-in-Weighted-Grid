# Robot-Pathfinding-in-Weighted-Grid

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/heitornolla/Robot-Pathfinding-in-Weighted-Grid/blob/main/jupyter-notebook/colab-notebook.ipynb)


# Overview

This code is related to the work "Navegação de Robôs em Grade Ponderada com Custos de Terreno Variáveis" conducted through FT-Unicamp's SI702 class.

This work addresses the path planning problem for a robot in a weighted grid, taking into account different types of terrain with varying movement costs. The problem is solved using search algorithms, including A*, Greedy Best-First Search, and Breadth-First Search. The study aims to compare the efficiency of these algorithms in terms of the number of nodes explored and the final path cost, considering terrain variability: water, grass, mud, and traffic. We detail the data structures used to model the problem and the implemented algorithms. All Python code generated for running the experiments is also provided. You may read the full work in Overleaf, although available only in Brazilian portuguese.

[![Read in Overleaf](https://img.shields.io/badge/Open%20in-Overleaf-brightgreen)](https://www.overleaf.com/read/vhsrphkqqtqn#644d10)

## Aside

If you're curious as to how the A* algorithm expands the nodes and the order in which they're visited, you can now see it clearly on this notebook:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/heitornolla/Robot-Pathfinding-in-Weighted-Grid/blob/main/jupyter-notebook/iterative_printing.ipynb)
