package org.bkpathak.ds.linklist;

/**
 * Created by bijay on 1/28/16.
 * Given the integer k, less then or equals the length of  k, rotate the
 * list.
 * Input: k= 2 , 1 -> 2 -> 3 -> 4 -> 5 -> NULL
 * Output: 3 -> 4 -> 5 -> 1 -> 2 -> NULL
 */

public class RotateList {

    public static LinkList rotateList(int k, LinkList list) {
        if (k >= list.length || list == null) {
            return list;
        }
        int count = 0;
        ListNode current = list.head;
        ListNode tempHead = null;
        while (current.next != null) {
            count++;
            if (count == k) {
                tempHead = current;
            }
            current = current.next;
        }
        current.next = list.head;
        list.head = tempHead.next;
        tempHead.next = null;
        return list;
    }

    public static void main(String[] args) {
        LinkList list = new LinkList();

        for (int i = 1; i <= 5; i++) {
            list.addAtEnd(i);
        }
        System.out.println("Before rotating:");
        list.display();
        RotateList.rotateList(2,list);
        System.out.println("After  rotation:");
        list.display();
    }
}
