package org.bkpathak.ds.graph;

import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.LinkedList;
import java.util.Stack;

/**
 * Created by bijay on 2/6/16.
 * Topological Sort using DFS and stack.
 */
public class TopologicalSort {
    private boolean[] visited;
    private Stack<Integer> stack;

    TopologicalSort(int v){
        visited = new boolean[v];
        stack = new Stack<Integer>();
    }

    /**
     * Topological sort
     */
    public void topologicalSort(Graph graph, int startV){
        // Clear the visited array
        Arrays.fill(visited, false);
        
    }
}

