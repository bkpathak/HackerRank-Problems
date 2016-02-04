package org.bkpathak.ds.linklist;

import sun.awt.image.ImageWatched;

/**
 * Created by bijay on 1/30/16.
 * Given two list representing the Number, represent the sum in third list.
 */
public class AddList {
    public static LinkList addList(LinkList l1, LinkList l2){
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        LinkList sumList = new LinkList();
        int carry = 0;
        int sum = 0;
        ListNode ln1 = l1.head;
        ListNode ln2 = l2.head;
        while(ln1 != null || ln2 != null){
            if(ln1 == null){
                sum = carry + ln2.val;
                ln2  = ln2.next;
            }
            else if(ln2 == null){
                sum = carry + ln1.val;
                ln1 = ln1.next;
            }
            else{
                sum = carry + ln1.val + ln2.val;
                ln1 = ln1.next;
                ln2 = ln2.next;
            }
            sumList.addAtEnd(sum % 10);
            carry = sum / 10;
        }
        if(carry !=0){
            sumList.addAtEnd(carry);
        }
        return sumList;
    }

    public static void main(String[] args){
        LinkList l1 = new LinkList();
        LinkList l2 = new LinkList();
        // n1 = 378;    8 -> 7 -> 3 -> NULL
        // n2 = 755;    5 -> 5 -> 5 -> NULL
        // sum = 1133;  3 -> 3 -> 1 -> 1 -> NULL
        l1.addAtFront(3);
        l1.addAtFront(7);
        l1.addAtFront(8);
        l2.addAtFront(7);
        l2.addAtFront(5);
        l2.addAtFront(5);
        System.out.println("First List:");
        l1.display();
        System.out.println("Second List");
        l2.display();
        LinkList sumList = AddList.addList(l1,l1);
        System.out.println("Sum List");
        sumList.display();
    }
}
