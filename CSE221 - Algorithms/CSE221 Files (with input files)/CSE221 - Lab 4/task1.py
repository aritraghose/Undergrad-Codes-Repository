# Task 1

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:18:13 2022

@author: Rubayat Khan
"""
# CSE221 Lab 03 Graphs

def readFile():
    # reading file from as input
    # change the file name according to yours
    f = open("/content/sample_data/graph.txt", "r")
    
    # first line of input contains the number of vertices in the graph
    n = f.readline()
    # strip() gets rid of the new line
    # try printing n without strip()
    #print(n.strip())
    n = n.strip()
    #print(type(n))
    # n is of type string. we need to convert it to int
    n=int(n)
    #print(type(n))
    
    # the second line of the file contains the number of connections
    c = f.readline()
    c = c.strip()
    c = int(c)
    #print(c)

    buildGraphUsingDictionary(c,f)

    f = open("/content/sample_data/graph.txt", "r")
    n = int(f.readline().strip())
    c = int(f.readline().strip())

    buildGraphUsingListofLists(c,f)



# we want to build an adjacency list like the following
# A -> B,C 
# One vertex can be connected to multiple vertices
# which means multiple values are associated with one vertex
# one data structure that can be used is a dictionary of lists
# {A:[B,C]}

def buildGraphUsingDictionary(c,f): 
    # creating a dictionary
    graph = {}
    # the following lines of the file contain the connections
    # creating a directed graph (a,b means a is connected to b)
    
    counter = 0
    while (counter<c):
        line = f.readline() # reading each libe
        a,b = line.split(",") # splitting the vertices
        b = b.strip() # getting rid of \n from the end
        
        # we first search if the value inside variable a exists in the dictionary or not
        if(a in graph):
            # if yes, then append() the value in b to a
            graph[a].append(b)
        else:
            # create a new list in graph with a as the key and b as the value
            graph[a] = [b]
        #print(a)
        #print(b)
        counter+=1    
    
    print("Using Dictionary:", graph)
    printGraph(graph, None)
    print()
       
    
# TO DO
# This method must be completed by you
# You should code in such a way that the output should be
 # 1 -> 2,4
 # 2 -> 4
 # 3 -> 1,4
 # 4 -> 2
# notice this method takes both the graphs as parameters
# this means you have print the same output in the same style for both the datastructures
# if graph is none then print from listGraph
# if listGraph is none then print from graph
def printGraph(graph,listGraph):  
    # Your code
    output_file = open("/content/sample_data/output1.txt", "w")
    # it first writes the output on the .txt file for graph, then overwrites on the same .txt file for listGraph

    if (listGraph == None):
      for key, val in graph.items():
        vertices = ""
        for j in range(len(val)):
          vertices += (str(graph[key][j]) + ",")
        print(f"{key} -> {vertices[:-1]}")
        output_file.write(f"{key} -> {vertices[:-1]}\n")

    else:
      for i in range(len(listGraph)):
        if (len(listGraph[i]) != 0):
          vertices = ""
          for j in range(len(listGraph[i])):
            vertices += (str(listGraph[i][j]) + ",")
          print(f"{i} -> {vertices[:-1]}")
          output_file.write(f"{i} -> {vertices[:-1]}\n")
    output_file.close()



# TO DO
# I have shown you how to build a graph using a dictionary of list
# now your job is to build a graph using list of lists [[E,B],[C,D]]
# it means A -> E,B and B -> C,D
def buildGraphUsingListofLists(c,f):
    listGraph = [] # do not change the name of the variable
    
    # your code
    listGraph = [[] for i in range(c)]
    counter = 0

    while (counter < c):
      line = f.readline()
      a, b = line.split(",")
      a = int(a)
      b = int(b.strip())
      listGraph[a].append(b)
      counter += 1

    print("Using 2D List:", listGraph)
    printGraph(None,listGraph)



# ======================Program starts here.========================

# read file using the readFile() method
readFile()

