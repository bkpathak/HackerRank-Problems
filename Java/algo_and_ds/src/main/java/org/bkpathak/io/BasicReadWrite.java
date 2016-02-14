package org.bkpathak.io;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 * Created by bijay on 2/14/16.
 * Java File I/O implementation
 */
public class BasicReadWrite {
    public static void main(String[] args) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;
        try {
            in = new FileInputStream("/home/bijay/Desktop/Programs-Collections/" +
                    "Java/algo_and_ds/src/main/resources/Test.txt");
            out  = new FileOutputStream("/home/bijay/Desktop/Programs-Collections/" +
                    "Java/algo_and_ds/src/main/resources/Out.txt");

            int input;
            while((input = in.read()) != -1){
                out.write(input);
            }
        }finally {
            if (in != null){
                in.close();
            }if (out != null){
                out.close();
            }
        }
    }
}