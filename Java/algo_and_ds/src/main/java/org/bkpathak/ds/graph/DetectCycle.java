package org.bkpathak.ds.graph;

import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Iterator;

/**
 * Created by bijay on 2/6/16.
 */
public class DetectCycle {
    boolean[] visited;
    boolean[] recstack;

    DetectCycle(int v){
        visited = new boolean[v];
        recstack = new boolean[v];
    }

    /**
     * Utility functions to detect cycle
     */
    private boolean isCyclicDirectedUtil(Graph graph,int v){
        // Mark the current vertex as visited and put in the recursion stack
        visited[v] = true;
        recstack[v] = true;

        // Recur all the vertices adjacent to this vertices
        Iterator<Integer> itr = graph.iterator(v);

        while(itr.hasNext()){
            int n = itr.next();
            //  if visited , then it's already explored continue
            if(!visited[n] && isCyclicDirectedUtil(graph,n)){
                return true;
            }
            // if in recstack then cycle found
            if(recstack[n]){
                return true;
            }
        }
        // remove it from recstack since it is explored completely
        recstack[v] = false;
        return false;
    }

    /**
     * Detect cycle in directed graph
     */
    boolean isCyclicDirected(Graph graph, int startV){
        // Clear the visited and recstack array
        Arrays.fill(visited,false);
        Arrays.fill(recstack,false);
        return isCyclicDirectedUtil(graph,startV);
    }

    public static void main(String[] args){
        Graph graph = new Graph(7);
        DetectCycle cyl = new DetectCycle(7);
        graph.addEdge(0,1);
        graph.addEdge(0,4);
        graph.addEdge(1,2);
        graph.addEdge(2,3);
        graph.addEdge(4,5);
        graph.addEdge(5,2);
        graph.addEdge(5,6);
        //graph.addEdge(3,5);

        if (cyl.isCyclicDirected(graph,0)){
            System.out.println("Graph has cycle");
        }
        else{
            System.out.println("Graph doesn't has cycle");
        }
    }
}
