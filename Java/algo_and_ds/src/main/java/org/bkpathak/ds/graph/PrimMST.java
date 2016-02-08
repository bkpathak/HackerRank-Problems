package org.bkpathak.ds.graph;

import java.util.*;

/**
 * Created by bijay on 2/7/16.
 * Prim's MST implementation using Priority Queue
 * O(n) : O(E log v)
 */
public class PrimMST {
    boolean[] visited;
    int vertex; // number of vertex in graph
    PriorityQueue<WeightedGraph.Node> queue;
    int[] parent; // To store the MST

    PrimMST(int v) {
        vertex = v;
        visited = new boolean[v];
        // Implements anonymous Comparator class
        queue = new PriorityQueue<WeightedGraph.Node>(v, new Comparator<WeightedGraph.Node>() {
            public int compare(WeightedGraph.Node o1, WeightedGraph.Node o2) {
                if (o1.weight == o2.weight) {
                    return 0;
                } else if (o1.weight < o2.weight) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });

        parent = new int[v];
        Arrays.fill(parent, -1);
    }

    /**
     * Algorithm
     * 1. while count < vertices
     * if current node not visited
     * mark it visited
     * push all its edges to the PriorityQueue if not visited
     * extract the minimum edge from PriorityQueue
     * if the minimum edge leads to an unvisited vertex
     * add it to MST
     * current = newVertex
     * ++count
     * else
     * extract the minimum edge from PriorityQueue again
     * if the minimum edge leads to an unvisited vertex
     * add it to MST
     * current = newVertex
     */

    public void primMST(WeightedGraph graph, int startV) {
        int i = 0;
        int current = startV;
        WeightedGraph.Node tempNode, minNode;
        int src, dst;

        while (i < vertex) {
            if (!visited[current]) {
                visited[current] = true;
                // Traverse all the adjacent nodes of the current Nodes
                Iterator<WeightedGraph.Node> itr = graph.getIterator(current);

                while (itr.hasNext()) {
                    tempNode = itr.next();

                    if (!visited[tempNode.dest]) {
                        // Add it to queue
                        queue.add(tempNode);
                    }
                }
                // Get the minimum edge from the queue
                minNode = queue.poll();
                src = minNode.src;
                dst = minNode.dest;
                if (!visited[dst]) {
                    parent[dst] = src;
                }
                current = dst;
                i++;
            } else {
                minNode = queue.poll();
                src = minNode.src;
                dst = minNode.dest;
                if (!visited[dst]) {
                    parent[dst] = src;
                }
                current = dst;
            }
        }

    }

    /**
     * Print the MST
     */
    public void displayMST() {
        System.out.println("Prim's MST:");
        for (int i = 0; i < vertex; i++) {
            System.out.println(parent[i] + " -> " + i);
        }
    }

    public static void main(String[] args) {
        WeightedGraph graph = new WeightedGraph(9);
        graph.addEdge(0, 1, 4);
        graph.addEdge(0, 7, 8);
        graph.addEdge(1, 2, 8);
        graph.addEdge(1, 7, 11);
        graph.addEdge(2, 3, 7);
        graph.addEdge(2, 8, 2);
        graph.addEdge(2, 5, 4);
        graph.addEdge(3, 4, 9);
        graph.addEdge(3, 5, 14);
        graph.addEdge(4, 5, 10);
        graph.addEdge(5, 6, 2);
        graph.addEdge(6, 7, 1);
        graph.addEdge(6, 8, 6);
        graph.addEdge(7, 8, 7);

        PrimMST mst = new PrimMST(9);
        mst.primMST(graph,0);
        mst.displayMST();
    }

}
