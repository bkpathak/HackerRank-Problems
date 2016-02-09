package org.bkpathak.ds.graph;

import java.util.*;

/**
 * Created by bijay on 2/8/16.
 * Implement the Dijkstra's algorithm for the Adjacency List
 * Complexity: O(n) = O(E log V)
 */
public class DijkstraAdjList {

    class Node {
        int vrtx; // vertex
        double dst; // distance

        Node(int v, double d) {
            vrtx = v;
            dst = d;
        }
    }

    double[] dist; // Stores the distance
    int vertex; // number of vertex in graph
    PriorityQueue<Node> queue;
    int[] parent; // To store the the parent
    boolean[] visited; // Tos tore the vertex already explored
    Node[] vertexLocation; // Stores the location of the vertex.

    DijkstraAdjList(int v) {
        vertex = v;
        dist = new double[v];
        queue = new PriorityQueue<Node>(v, new Comparator<Node>() {
            public int compare(Node o1, Node o2) {
                if (o1.dst == o2.dst) {
                    return 0;
                } else if (o1.dst < o2.dst) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });

        vertexLocation = new Node[v];
        // Create the New Node and add it to the queue
        for (int i = 0; i < v; i++) {
            Node temp = new Node(i, Integer.MAX_VALUE);
            queue.add(temp);
            vertexLocation[i] = temp;
        }

        parent = new int[v];
        visited = new boolean[v];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
        Arrays.fill(visited, false);
    }

    /**
     * Find the Dijkstra's shortest path for the graph
     * represented with Adjacency List
     */
    public void dijkstraShortestPath(WeightedGraph graph, int srcV) {
        // Set the distance of source vertex to 0
        dist[srcV] = 0;

        // Create the new Node and add it to the queue with distance
        queue.add(new Node(srcV, 0));

        Node minNode;
        WeightedGraph.Node currNode;
        int currU; // Current vertex

        // Loop until the Priority Queue is empty
        while (!queue.isEmpty()) {
            // Extract the Node with minimum distance from queue
            minNode = queue.poll();
            currU = minNode.vrtx;
            visited[currU] = true;

            // Traverse through all the vertex of currV and update the distance
            Iterator<WeightedGraph.Node> itr = graph.getIterator(currU);
            while (itr.hasNext()) {
                currNode = itr.next();
                int v = currNode.dest;
                double wght = currNode.weight;

                // Update the all the node reachable from currV if:
                // 1. currV is already relaxed( dist[currV] != Integer.MAX_VALUE)
                // 2. distance to vertex V, through currV is less than previously calculated
                // 3. vertex is not visited
                if (dist[currU] != Integer.MAX_VALUE && dist[currU] + wght < dist[v]) {
                    dist[v] = dist[currU] + wght;
                    // Update the parent
                    parent[v] = currU;
                    // Update the node dist in queue
                    // 1. First extract the node form the queue
                    // 2. Update the node
                    // 3. Reinsert the node
                    queue.remove(vertexLocation[v]);
                    Node temNode = new Node(v,dist[v]);
                    vertexLocation[v]= temNode;
                    queue.add(temNode);
                }
            }
        }
    }

    /**
     * Print the distance from the source
     */
    public void displayDistance() {
        System.out.println("Vertex \t Distance from source");
        for (int i = 0; i < vertex; i++) {
            System.out.println(i + " \t\t " + dist[i]);
        }
    }

    /**
     * Print the Shortest Path
     */
    /**
     * Print the MST
     */
    public void displayPath() {
        System.out.println("Shortest Path:");
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

        DijkstraAdjList dijkstraAdjList = new DijkstraAdjList(9);
        dijkstraAdjList.dijkstraShortestPath(graph, 0);
        dijkstraAdjList.displayDistance();
        dijkstraAdjList.displayPath();



    }
}
