package org.bkpathak.ds.bst;

/**
 * Created by bijay on 2/4/16.
 */

import java.util.Scanner;

public class NodeDistance {
    class Node {
        int val;
        Node left;
        Node right;

        Node(int val) {
            this.val = val;
            left = null;
            right = null;
        }
    }

    Node root = null;

    /**
     * Add new Node to the tree reccursively.
     */
    private void addNode(Node current, int val){
        if (val < current.val) {
            if(current.left == null){
                current.left = new Node(val);
            }
            else{
                addNode(current.left,val);
            }
        }else{
            if (current.right ==null){
                current.right = new Node(val);
            }
            else{
                addNode(current.right,val);
            }
        }
    }

    /**
     * Traverse the array and add each element to the tree.
     */
    public void createBST(int[] array) {
        for (Integer e : array) {
            // If this is the first node
            if(root == null){
                root =new  Node(e);
            }
            else {
                addNode(root, e);
            }
        }
    }

    /**
     * Find the depth of the node from the root
     */
    private int findDepth(Node current, int k, int depth) {
        // Base case
        if (current == null) {
            return -1;
        }
        // If present return the height
        if (current.val == k) {
            return depth;
        }
        if (k < current.val) {
            return findDepth(current.left, k, depth + 1);
        } else {
            return findDepth(current.right, k, depth + 1);
        }
    }

    /**
     * Find the least common ancestor of the the given two node
     */

    private Node findLCA(Node current, int k1, int k2) {
        // Base case
        if (current == null) {
            return null;
        }
        // If the key matches return the node
        if (current.val == k1 || current.val == k2) {
            return current;
        }

        Node leftAncestor = findLCA(current.left, k1, k2);
        Node rightAncestor = findLCA(current.right, k1, k2);

        if (leftAncestor != null && rightAncestor != null) {
            return current;
        }
        return leftAncestor != null ? leftAncestor : rightAncestor;
    }

    public int findDistance(int k1, int k2) {
        // Find the depth of key1 node
        int d1 = findDepth(root, k1, 0);
        // Find the depth  of key2 node
        int d2 = findDepth(root, k2, 0);

        // If either d1 or d2 is -1 , then either or both node are not present in the tree
        if (d1 == -1 || d2 == -1) {
            return -1;
        }
        // Find the common ancestor of the k1 and k2
        Node lcaNode = findLCA(root, k1, k2);

        // find the depth of LCA Node
        int lcaDepth = findDepth(root, lcaNode.val, 0);

        // Now find the distance between two node
        // distance  = d1 + d2 - 2 * lcaDepth
        int nodeDist = (d1 + d2) - (2 * lcaDepth);

        return nodeDist;

    }

    public static void main(String args[]) throws Exception {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

        NodeDistance sol = new NodeDistance();
        Scanner sc = new Scanner(System.in);
        // Read First Node
        int A = sc.nextInt();
        // Read Second Node
        int B = sc.nextInt();
        // Read number of Nodes
        int n = sc.nextInt();
        // Ignore the new line
        sc.nextLine();

        // Read all the node value
        String numberInput = sc.nextLine();

        // Split the node value
        String[] inputSplit = numberInput.split(" ");

        // Create the array to hold the value of the node
        int[] nodeVal = new int[n];

        // add the value to the array
        for (int i = 0; i < n; i++) {
            nodeVal[i] = Integer.parseInt(inputSplit[i]);
        }

        // Create the BST
        sol.createBST(nodeVal);

        // Find the distance between two nodes A and B
        int nodeDist = sol.findDistance(A, B);

        if (nodeDist == -1) {
            System.out.println("Not found");
        } else {
            System.out.println(nodeDist);
        }
    }
}