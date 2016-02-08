package org.bkpathak.ds.graph;


import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * Created by bijay on 2/7/16.
 */
public class WeightedGraph {
    class Node{
        int src;
        int dest;
        double weight;
        Node(int s,int d, double w){
            src = s;
            dest = d;
            weight = w;
        }
    }

    ArrayList<LinkedList<Node>> adjList;
    int vertex ; // Number of vertex in graph

    WeightedGraph(int v){
        vertex = v;
        adjList = new ArrayList<LinkedList<Node>>(v);
        for(int i =0 ; i < v ; i++){
            adjList.add(new LinkedList<Node>());
        }
    }

    /**
     * Add the new Node to the adjList
     */
    public void addEdge(int src, int dst, double wght){
        adjList.get(src).add(new Node(src,dst,wght));
    }

    /**
     * Return the iterator
     */

    public Iterator<Node> getIterator(int v){
        return adjList.get(v).iterator();
    }

}
