# Brief Description of the Python Code for Implementing Graphs

Note that hw4 folder contains 7 python files. Following is a brief description of the functionality of each of these files:
* problem_1.py: Template where you can implement your solutions to Problem 1
* problem_2.py: Template where you can implement your solutions to Problem 2
* graph.py: Represents the input graph as an abstract data structure; Allows us to create new graphs, add new edges to an existing graph, or get any specific attribute-information (e.g. edge weight).
* list_to_graph.py: Converts any graph input represented in the form of a adjacency list into the graph data structure. 
* matrix_to_graph.py: Converts any graph input represented in the form of a adjacency matrix into the graph data structure. 
* edge.py: Definition of an edge
* vertex.py: Definition of a vertex

# Submission Instructions

Students should submit their written assignments as a pdf document with the title "hw4-sol.pdf" (either a scanned copy of hand-written version, or created using the provided LaTeX template), with the name written on the top left corner of the first page. 

# Instructions for Cloning hw4 folder

Students will be given access to the Git repository as 'developers'. As a result, they can clone the master branch and submit their respective assignments by following the procedure given below:

## Execute once, to clone a repository:
```
$ git clone https://git-classes.mst.edu/2018-FS-CS2500/hw4-<student-id>
```

## Execute as many times as you like from within the directory/repository you cloned to your hard drive (just an example):
```
# To check the status of your repository:
$ git status

# To stage/add a file:
$ git add *.py *.pdf *.md

# To add a folder:
$ git add SUBDIRECTORY/*

# To commit changes and document them:
$ git commit -m "Informative description of the commit"

# To submit your assignments:
$ git push
```




## Do not add:
Compiled or generated files like *.out, *.log, *.syntex.gz, *.bib, your executable files, etc. Put the name of these files in a text file named .gitignore 

If you see your changes reflected on the git-classes site, you have submitted successfully.

## Useful links:
[Git Cheatsheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

[Videos on Git basics](https://git-scm.com/videos)