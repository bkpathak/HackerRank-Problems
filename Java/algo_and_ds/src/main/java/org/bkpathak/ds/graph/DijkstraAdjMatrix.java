package org.bkpathak.ds.graph;

import java.util.Arrays;

/**
 * Created by bijay on 2/7/16.
 * Implements the Dijkstra's for the Adjacency Matrix
 * Complexity O(n) = O(V ^ 2)
 */
public class DijkstraAdjMatrix {
    int vertex;
    boolean[] shortestPathSet;
    int[] dist;
    int[] parent; // To store the path from source to dist

    DijkstraAdjMatrix(int v) {
        shortestPathSet = new boolean[v];
        dist = new int[v];
        parent = new int[v];
        vertex = v;
        Arrays.fill(shortestPathSet, false);
        Arrays.fill(dist, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
    }

    /**
     * Find the min distance from the vertex that are not present in
     * the shortestPathSet
     */
    private int findMinDistance() {
        int min = Integer.MAX_VALUE;
        int minIndex = -1;

        for (int v = 0; v < vertex; v++) {
            if (!shortestPathSet[v] && dist[v] < min){
                min = dist[v];
                minIndex = v;
            }
        }
        return  minIndex;
    }

    /**
     * Implements the Dijkstra's single source shortest path algorithm for a
     * graph represented as Adjacency Matrix.
     */
    public void dijkstraShortestPath(int[][] graph, int src){

        // Set the distance of the src vertex, which is 0 frm itself
        dist[src] = 0;

        //Find the shortest path for all the vertices

        for(int i =0; i < vertex; i++){
            // Choose the minimum distance vertex from the dist which is not yet
            // in shortestPathSet
            int u = findMinDistance();

            // If the u is equals to dest node, we found source to destination path; break the loop
            //if(u == dst){
            //     break;
            // }

            // Mark this vertex as processed; this is similar to visited in DFS and BFS
            shortestPathSet[u] = true;

            // Now update the distance of the all the adjacent vertices of the
            // vertex u

            for (int v = 0; v < vertex; v++){
                // Update the vertex if it's not processed and there is
                // edge from u to v and distance from source to v through
                // u is less than current v
                if(!shortestPathSet[v]){
                    if(graph[u][v] != 0 && dist[u] != Integer.MAX_VALUE &&
                            dist[u] + graph[u][v] < dist[v]){
                        dist[v] = dist[u] + graph[u][v];
                        // Update the parent for the vertex
                        parent[v] = u;
                    }
                }
            }

        }

    }

    /**
     * Print the distance from the source
     */
    public void displayDistance(){
        System.out.println("Vertex \t Distance from source");
        for(int i =0; i < vertex; i++){
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

    public static void main(String[] args){
        DijkstraAdjMatrix spt = new DijkstraAdjMatrix(9);
        int[][] graph = new int[][]{{0, 4, 0, 0, 0, 0, 0, 8, 0},
                {4, 0, 8, 0, 0, 0, 0, 11, 0},
                {0, 8, 0, 7, 0, 4, 0, 0, 2},
                {0, 0, 7, 0, 9, 14, 0, 0, 0},
                {0, 0, 0, 9, 0, 10, 0, 0, 0},
                {0, 0, 4, 0, 10, 0, 2, 0, 0},
                {0, 0, 0, 14, 0, 2, 0, 1, 6},
                {8, 11, 0, 0, 0, 0, 1, 0, 7},
                {0, 0, 2, 0, 0, 0, 6, 7, 0}
        };

        spt.dijkstraShortestPath(graph,0);
        spt.displayDistance();
        spt.displayPath();
    }

}
