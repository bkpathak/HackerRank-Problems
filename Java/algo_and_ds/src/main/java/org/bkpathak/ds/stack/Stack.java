package org.bkpathak.ds.stack;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by bijay on 2/5/16.
 * Basic implementation of stack
 */
public class Stack<E> {
    private List<E> elementData;
    private int size;
    private int top;


    Stack(int capacity) {
        this.top = -1;
        this.size = capacity;
        elementData = new ArrayList<E>(capacity);
    }

    /**
     * Check if the stack is full
     */
    private boolean isFull() {
        return top == size-1;
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
        elementData.add(++top,item);
    }

    /**
     * pop the element from the top of the stack
     */
    public E pop(){
        if(isEmpty()){
            System.out.println("Stack is empty");
            System.exit(-1);
        }
        return elementData.get(top--);
    }

    /**
     * Shows the item at the top of the stack
     */
    public E peek(){
        if(isEmpty()){
            System.out.println("Stack empty");
            System.exit(-1);
        }
        return elementData.get(size);
    }

    public static void main(String[] args){
        Stack<Integer> stack = new Stack(5);
        //stack.pop();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        //stack.push(6);
        //stack.push(7);
    }

}

