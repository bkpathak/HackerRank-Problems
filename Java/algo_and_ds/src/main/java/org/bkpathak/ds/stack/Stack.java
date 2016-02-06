package org.bkpathak.ds.stack;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bijay on 2/5/16.
 * Basic implementation of stack which returns minimum element in stack in O(1) time.
 */
public class Stack<E extends Comparable<E>> {
    private List<E> elementData;
    private List<E> minData;
    private int size;
    private int top;


    Stack(int capacity) {
        this.top = -1;
        this.size = capacity;
        elementData = new ArrayList<E>(capacity);
        minData = new ArrayList<E>(capacity);
    }

    /**
     * Check if the stack is full
     */
    private boolean isFull() {
        return top == size - 1;
    }

    /**
     * Check if the stack is empty
     */
    private boolean isEmpty() {
        return top == -1;
    }

    /**
     * Push elements to the stack
     */
    public void push(E item) {
        if (isFull()) {
            System.out.println("Stack full");
            System.exit(-1);
        }
        elementData.add(++top, item);

        if (minData.size() == 0) {
            minData.add(item);
        } else {
            if (item.compareTo(minData.get(minData.size() - 1)) <= 0) {
                minData.add(item);
            }
        }
    }

    /**
     * pop the element from the top of the stack
     */
    public E pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            System.exit(-1);
        }
        E item = elementData.get(top--);
        if (item.compareTo(minData.get(minData.size() - 1)) <= 0) {
            minData.remove(minData.size() - 1);
        }
        return item;
    }

    /**
     * Shows the item at the top of the stack
     */
    public E peek() {
        if (isEmpty()) {
            System.out.println("Stack empty");
            System.exit(-1);
        }
        return elementData.get(size);
    }

    /**
     * Shows the top min data present in stack
     */
    public E getMin() {
        if (isEmpty()) {
            System.out.println("Stack Empty");
            System.exit(-1);
        }
        return minData.get(minData.size() - 1);
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack(5);
        //stack.pop();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        System.out.println("Min element: " + stack.getMin());
        //stack.push(6);
        //stack.push(7);
    }

}

