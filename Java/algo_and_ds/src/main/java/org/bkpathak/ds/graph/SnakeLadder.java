package org.bkpathak.ds.graph;


import java.util.Arrays;
import java.util.LinkedList;

/**
 * Created by bijay on 2/7/16.
 * Finds the minimum number of throws required to reach destination from source.
 */
public class SnakeLadder {
    boolean[] visited;
    int N; // Number of vertex;

    SnakeLadder(int v){
        // Used 1 based index
        N = v;
        visited = new boolean[v+1];
        Arrays.fill(visited,false);
    }
    class Node{
        int vertex; // vertex number
        int dist; // Distance of this vertex from source
        Node(int v,int d){
            vertex = v;
            dist = d;
        }
    }

    /**
     * This algorithm uses BFS. The minimum distance of unweighted graph can be found using BFS and
     * for the game all the dice throw(1,6) will be at same level from the source.
     */
    public int findMinDistance(int[] graph){
        // Clear the visited array
        Arrays.fill(visited, false);
        // Create queue for BFS
        LinkedList<Node> queue = new LinkedList<Node>();

        // Mark the first node as visited and add it to the queue
        visited[1] = true;
        Node currN = new Node(1,0);
        queue.add(currN);

        int currV;
        while(!queue.isEmpty()){

            // Get the first element from the queue
            currN = queue.poll();
            currV = currN.vertex;

            // If the current vertex is the target vertex; then we reached the destination.
            if(currV == N){
                break;
            }

            // Enqueue all the vertices reachable from the current vertices to the queue.
            for(int j = currV + 1; j <= (currV + 6) && j <= N; j++ ){
                // If the adjacent vertex is not visited
                if (!visited[j]){
                    // Calculate the distance of the vertex j
                    int d = currN.dist + 1;
                    // Check if the vertex contains any ladder or snake
                    int v;
                    if(graph[j] !=-1){
                        v = graph[j];
                    }else{
                        v = j;
                    }
                    // Create the Node and add it to the queue
                    queue.add(new Node(v,d));
                }
            }
        }
        // We found the last vertex return the distance
        return currN.dist;
    }

    public static void main(String[] args){
        // Size of the board game
        int N = 30;
        // Create the graph of size N+1 , 1 based index
        int[] graph = new int[N+1];
        // Assign -1 to the graph indicating there is no snake or ladder
        Arrays.fill(graph,-1);

        // Now put the ladder on the board
        graph[3] = 21;
        graph[5] = 8;
        graph[11] = 26;
        graph[20] = 29;

        // Put the snake on the board
        graph[27] = 1;
        graph[21] = 8;
        graph[17] = 4;
        graph[19] = 7;

        SnakeLadder sl = new SnakeLadder(N);
        System.out.println("Min distance is: " + sl.findMinDistance(graph));
    }

}
