package org.bkpathak.algo;

/**
 * Created by bijay on 1/24/16.
 * Basic Least Recently Used Cache Implementation
 *
 */
public class LRUCache {
    // A QNode implemented using doubly LinkedList
    class QNode {
        QNode prev, next;
        long pageNumber;

        QNode(long pageNumber) {
            this.pageNumber = pageNumber;
            this.prev = null;
            this.next = null;
        }
    }

    // A Hash pointing to the QNode
    class Hash {
        int capacity; // Capacity of Hash
        QNode[] array; // An array of QNode

        Hash(int capacity) {
            this.capacity = capacity;
            // Array of pointers to refer to QNode
            this.array = new QNode[capacity];
            //Initialize it to NULL
            for (int i = 0; i < this.capacity; i++) {
                this.array[i] = null;
            }
        }
    }

    // A Cache implementation of QNode
    int count; // Number of filled frames in Cache
    int totalFrame; // Total number of frame available
    QNode front, rear;

    // Create Queue to hold at most totalFrame
    LRUCache(int totalFrame) {
        this.count = 0;
        this.front = this.rear = null;
        this.totalFrame = totalFrame;
    }


    // Check if the frames are full or not.
    boolean areFramesFull(){
        return this.count == this.totalFrame;
    }


    // Check if Cache is empty
    boolean isCacheEmpty(){
        return this.rear == null;
    }


    // Delete frame from Cache(Queueu)
    // We'll always remove from the rear of the cache list
    void deleteFrame(){
        if (!isCacheEmpty()){
            // If this is only node in cache , then change front
            if (this.front == this.rear){
                this.front = null;
            }

            //Move the rear to previous
            this.rear = rear.prev;
            // Set the rear next to null
            this.rear.next = null;

            // Decrease the count of frames in cache
            this.count --;
        }
    }


}
