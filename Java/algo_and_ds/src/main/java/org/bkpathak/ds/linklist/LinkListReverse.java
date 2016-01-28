package org.bkpathak.ds.linklist;

/**
 * Created by bijay on 1/27/16.
 */
public class LinkListReverse {
    class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
        }
    }

    Node head;

    LinkListReverse() {
        this.head = null;
    }

    /**
     * @param val Add the newNode at the beginning of the head.
     */
    public void addNodeAtFront(int val) {
        Node newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
    }

    /**
     * Reverse the List
     */
    public void reverseList() {
        Node previous = null;
        Node nextNode;
        Node current = this.head;
        while (current != null) {
            nextNode = current.next;
            current.next = previous;
            previous = current;
            current = nextNode;
        }
        this.head = previous;
    }


    public void reverseListRecur() {
        Node temp = this.head;
        reverseListRecurUtil(temp);
    }

    private void reverseListRecurUtil(Node current) {
        if (current.next == null) {
            this.head = current;
        } else {
            reverseListRecurUtil(current.next);
            current.next.next = current;
            current.next = null;
        }
    }

    public void display() {
        Node current = this.head;

        System.out.print("head");
        while (current != null) {
            System.out.print("->");
            System.out.print(current.val);
            current = current.next;
        }
        System.out.println("->NULL");
    }

    public static void main(String[] args) {
        LinkListReverse list = new LinkListReverse();
        list.addNodeAtFront(1);
        list.addNodeAtFront(2);
        list.addNodeAtFront(3);
        list.addNodeAtFront(4);
        list.addNodeAtFront(5);
        System.out.println("Original List");
        list.display();
        list.reverseListRecur();
        System.out.println("Reverse List:");
        list.display();
    }
}
