package org.bkpathak.ds.graph;

import java.util.*;

/**
 * Created by bijay on 2/6/16.
 * Topological Sort using DFS and stack.
 */
public class TopologicalSort {
    private boolean[] visited;
    private Stack<Integer> stack;

    TopologicalSort(int v) {
        visited = new boolean[v];
        stack = new Stack<Integer>();
    }

    /**
     * Sort Util
     */

    private void topologicalSortUtil(Graph graph, int v) {
        visited[v] = true;
        // Recurse through all the adjacent node
        Iterator<Integer> itr = graph.iterator(v);

        while (itr.hasNext()) {
            Integer n = itr.next();
            if (!visited[n])
                topologicalSortUtil(graph, n);
        }
        // Now push the node v to the stack since all its adjacent nodes are
        // explored.
        stack.push(v);
    }

    /**
     * Topological sort
     */
    public void topologicalSort(Graph graph, int startV) {
        // Clear the visited array
        Arrays.fill(visited, false);
        for (int i = 0; i < 6; i++) {
            if (!visited[i]) {
                topologicalSortUtil(graph, i);
            }
        }
        display();
    }

    /**
     * Display the content of the stack
     */
    private void display() {
        while (!stack.empty()) {
            System.out.print(stack.pop() + " ");
        }
    }

    public static void main(String[] args) {
        TopologicalSort tSort = new TopologicalSort(7);
        Graph g = new Graph(7);
        g.addEdge(5, 2);
        g.addEdge(5, 0);
        g.addEdge(4, 0);
        g.addEdge(4, 1);
        g.addEdge(2, 3);
        g.addEdge(3, 1);
        tSort.topologicalSort(g, 0);
    }
}

