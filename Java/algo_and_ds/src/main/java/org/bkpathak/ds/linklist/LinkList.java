package org.bkpathak.ds.linklist;

/**
 * Created by bijay on 1/28/16.
 * Base class for Link List
 * Provides Method to create, add and remove node in list
 */
public class LinkList {
    ListNode head;
    ListNode tail;
    int length;

    LinkList(){
        this.head  = null;
        this.tail = null;
        this.length = 0;
    }

    /**
     * Add node at the front of the list
     */
    public void addAtFront(int val){
        ListNode newNode = new ListNode(val);
        // Set the tail if it's the very first node.
        if(tail == null){
            tail = newNode;
        }
        newNode.next = this.head;
        this.head = newNode;
        length ++;
    }

    /**
     * Add node at the front of the List.
     */
    public void addAtEnd(int val){
        ListNode newNode = new ListNode(val);
        // Set the head Node if it's the very first Node
        if (head == null && tail == null){
            head = newNode;
            tail = newNode;
        }
        else{
            tail.next = newNode;
            tail = newNode;
        }
        length ++;
    }


    /**
     * Traverse the link list
     */
    public void display(){
        ListNode current = head;

        while(current != null){
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.print("NULL\n");
    }
}
