package org.bkpathak.algo.string;

import java.util.BitSet;

/**
 * Created by bijay on 2/11/16.
 * Given a String check if it's the Anagram of palindrome or not.
 * example : AAYYK is anagram of KAYAK
 *         : SETTLE is no a anagram of any palindrome string
 */
public class AnagramsOfPalindrome {
    public static boolean isAnagramOfPalindrome(String input){
        BitSet bitSet = new BitSet(26);
        input = input.toLowerCase();
        for(int i =0; i < input.length(); i++){
            char ch = input.charAt(i);
            bitSet.flip(ch);
        }
        return bitSet.cardinality() <=1;
    }

    public static void main(String[] args){
        String[] string = {"AAYYK","SETTLE"};
        for(String s: string ){
            if(AnagramsOfPalindrome.isAnagramOfPalindrome(s)){
                System.out.println(s + " is a anagram of palindrome.");
            }else{
                System.out.println(s + " is NOT a anagram of palindrome.");
            }
        }
    }
}
