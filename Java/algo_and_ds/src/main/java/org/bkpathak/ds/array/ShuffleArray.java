package org.bkpathak.ds.array;

import java.util.Random;

/**
 * Created by bijay on 2/14/16.
 * Implementation of Fisher-Yates  Shuffling algorithm
 */
public class ShuffleArray {
    public static void main(String[] args) {
        char[] array = {'A', 'B', 'C', 'D'};
        Random rand = new Random(19);
        char temp;
        for (int i = array.length - 1; i > 0; i--) {
            int n = rand.nextInt(i + 1);
            // Exchange Element
            temp = array[i];
            array[i] = array[n];
            array[n] = temp;
        }
        System.out.println(array);
    }
}
