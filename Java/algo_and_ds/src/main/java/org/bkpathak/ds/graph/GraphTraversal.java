package org.bkpathak.ds.graph;

import java.util.*;

/**
 * Created by bijay on 2/6/16.
 * Depth First Implementation
 */
public class GraphTraversal {
    boolean[] visited;

    GraphTraversal(int v){
        visited = new boolean[v];
    }

    /**
     * DFS util function
     */
    public void dfsUtil(Graph graph,int v){
        // Set the current vertex as visited
        visited[v] = true;
        // Print the current vertex.
        System.out.print(v + " ");

        // visit all the adjacent node of this vertex
        Iterator<Integer> itr = graph.iterator(v);
        while(itr.hasNext()){
            int nextVertex = itr.next();
            if (!visited[nextVertex]){
                dfsUtil(graph,nextVertex);
            }
        }
    }

    public void dfs(Graph graph,int startVertex){
        // clear the visited array
        Arrays.fill(visited,false);
        dfsUtil(graph,startVertex);
    }

    /**
     * BFS search
     */

    public void bfs(Graph graph, int startV){
        // Clear the visited array
        Arrays.fill(visited,false);

        // Queue for BFS
        LinkedList<Integer> queue = new LinkedList<Integer>();

        // Add the first vertex to the queue
        queue.add(startV);

        // Mark the startV as visited
        visited[startV] = true;
        while(!queue.isEmpty()){
            // Get the first element from the queue and print it
            int currentV = queue.poll();
            System.out.print(currentV + " ");
            Iterator<Integer> itr = graph.iterator(currentV);

            // Loop through all the adjacent vertices
            while(itr.hasNext()){
                
            }
        }

    }

    public static void main(String[] args){
        Graph graph = new Graph(5);
        GraphTraversal gTraverse = new GraphTraversal(5);
        graph.addEdge(0,1);
        graph.addEdge(0,4);
        graph.addEdge(0,2);
        graph.addEdge(1,3);
        graph.addEdge(3,2);
        graph.addEdge(4,2);
        // DFS graph traverse
        System.out.println("DFS traversal of graph starting at the vertex " + 0);
        gTraverse.dfs(graph,0);

    }
}
