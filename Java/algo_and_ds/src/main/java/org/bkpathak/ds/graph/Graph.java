package org.bkpathak.ds.graph;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * Simple Adjacency Graph implementation for used in Graph Algorithms
 */
public class Graph{
    int vertex; // No of vertices in graph
    ArrayList<ArrayList<Integer>> adjacecyList; // Adjacency List

    Graph(int v){
        vertex = v;
        adjacecyList = new ArrayList<ArrayList<Integer>>(v);
        for(int i =0; i < v; i++){
            adjacecyList.add(new ArrayList<Integer>());
        }
    }

    /**
     * Add edge to the vertex in graph
     */
    void addEdge(int v, int e){
        adjacecyList.get(v).add(e);
    }

    /**
     * Print the Graph Adjacency List representation
     */
    void printGraph(){
        for(int i = 0; i < vertex; i++){
            System.out.print("Vertex " + i +" : ");
            for(int j = 0;j < adjacecyList.get(i).size(); j++){
                System.out.print( adjacecyList.get(i).get(j) + " ");
            }
            System.out.print("\n");
        }
        System.out.print("\n");
    }

    /**
     * Return the iterator for the graph list
     */
    public Iterator<Integer> iterator(int v){
        return adjacecyList.get(v).listIterator();
    }
}