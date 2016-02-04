package org.bkpathak.ds.linklist;

/**
 * Created by bijay on 2/3/16.
 * Swap the every two nodes of the list
 * Input  : head -> 1 -> 2 -> 3 -> 4 -> NULL
 * Output : head -> 2 -> 1 -> 4 -> 3 -> NULL
 */
public class SwapNode {

    public static LinkList swapNode(LinkList list){
        if(list.head == null || list.head.next == null){
            return list;
        }

        // Assign current node pointed by head to previous
        ListNode prev = list.head;
        // Assign second node in the list to current
        ListNode curr = list.head.next;
        // Change the head of list to point to the second node
        list.head = curr;
        ListNode nextNode = null;
        while(true){
            // Store the next node pointer
            nextNode  = curr.next;
            // Current next points to the previous node
            curr.next = prev;

            // Check if the nextNode is Null or the nextNode is the last node.
            if(nextNode == null || nextNode.next == null){
                prev.next = nextNode;
                break;
            }
            // Update the previous next to points to the nextNode
            prev.next = nextNode.next;

            // Update previous and next
            prev = nextNode;
            curr = prev.next;
        }
        return list;
    }

    public static void main(String[] args){
        LinkList list = new LinkList();
        for(int i = 1; i <=10; i++){
            list.addAtEnd(i);
        }
        System.out.println("Before swapping:");
        list.display();
        System.out.println("After swapping:");
        LinkList swapList = SwapNode.swapNode(list);
        swapList.display();
    }
}
