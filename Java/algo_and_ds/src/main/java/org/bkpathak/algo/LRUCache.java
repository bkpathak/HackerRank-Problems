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
        int pageNumber;

        QNode(int pageNumber) {
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
    Hash hash;

    // Create Queue to hold at most totalFrame
    LRUCache(int totalFrame) {
        this.count = 0;
        this.front = this.rear = null;
        this.totalFrame = totalFrame;
        this.hash = new Hash(totalFrame);
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


    // Add page to Cache and Hash.
    // We'll add the page at the front of the cache list
    // And put the page in the hash with pageNumber as Key
    void addFrame(int pageNumber){
        // If cache is full, remove the element from the rear of the cache list
        if (areFramesFull()){
           deleteFrame();
       }
        // Create the new node  with given page number
        QNode new_node = new QNode(pageNumber);
        // Add the node to the front of the queue
        new_node.next = this.front;

        // If cache is empty, change both front and rear to point to the new_node
        if (isCacheEmpty()){
            this.front = this.rear = new_node;
        }
        else{
            // Change the front to point to the new_node
            this.front.prev = new_node;
            this.front = new_node;
        }

        // Add page entry to the Hash
        this.hash.array[pageNumber] = new_node;

        // Increase the count of frames
        this.count ++;
    }


    // If page is not in cache; bring the page and add to the front of the cache.
    // If already present in cache; move the page to the front of the cache
    void referencePage(int pageNumber){
        QNode requestPage = this.hash.array[pageNumber];

        // If page is not in cache
        if (requestPage == null){
            this.addFrame(pageNumber);
        }
        else{
            // Page is already in cache; move it to the front of the cache.
            // First remove the page from it's current location
            requestPage.prev.next = requestPage.next;

            // Check if requestPage is the rear node in the cache list
            if (requestPage == this.rear){
                this.rear = requestPage.prev;
                this.rear.next = null;
            }

            // Put the requestPage at the front of the cache list
            requestPage.next = this.front;
            requestPage.prev = null;

            // Change the previous of current front to point to the requestPage
            this.front.prev = requestPage;

            // Change the front to point to the requestPage;
            this.front = requestPage;
        }
    }

    void displayCache(){
        // Display the current pages in Cache
        QNode temp = this.front;
        while(temp != null){
            System.out.print(temp.pageNumber + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args){
        // Create the LRU Cache of size 10
        LRUCache cache = new LRUCache(10);

        // Page referenced are numbered from 0 to 9.
        // The order of reference is
        // 3 -> 6 -> 8 -> 3 -> 1 -> 2 -> 6
        System.out.println("Page reference order: 3 -> 6 -> 8 -> 3 -> 1 -> 2 -> 6");

        cache.referencePage(3);
        cache.referencePage(6);
        cache.referencePage(8);
        System.out.print("Current pages in Cache: ");
        cache.displayCache();
        System.out.println("Page 3 is reference again.");
        cache.referencePage(3);
        cache.displayCache();
        cache.referencePage(1);
        cache.referencePage(2);
        cache.referencePage(6);
        System.out.print("Current pages in Cache: ");
        cache.displayCache();
    }
}
