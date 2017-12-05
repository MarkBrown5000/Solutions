
//Solution to Arrays: Left Rotation problem.
//NOTE:  This solution timed out on the HackerRank site.  I looked at they're solution which used the built in System.arraycopy()
//			method.  My solution works, but is not ideal.  The solution using arraycopy is commented out below my solution.

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();    
        }
        
        int newArray[] = rotate(a, k, n);
        for (int i = 0; i < newArray.length; i++){
            System.out.print(newArray[i] + " ");
        }
     
    }
    
    public static int[] rotate(int[] arr, int rotations, int length){
        if(rotations == length){
            return arr;
        }
        for(int j = 0; j < rotations; j++){
            int temp = 0;
            for(int i = 0; i < arr.length; i++){
                if (i == 0){
                    temp = arr[i];
                    arr[i] = arr[i + 1];
                }else if(i == arr.length - 1){
                    arr[i - 1] = arr[i];
                    arr[i] = temp;
                }else{
                    int temp2 = 0;
                    temp2 = arr[i - 1];
                    arr[i - 1] = arr[i];
                    arr[i] = temp2;
                }
            }
        }
        return arr;
    }
}

/*
import java.util.*;
import java.lang.System;

public class Solution {
    
    public static int[] rotateArray(int[] arr, int d){
        // Because the constraints state d < n, we need not concern ourselves with shifting > n units.
        int n = arr.length;
        
        // Create new array for rotated elements:
        int[] rotated = new int[n]; 
        
        // Copy segments of shifted elements to rotated array:
        System.arraycopy(arr, d, rotated, 0, n - d);
        System.arraycopy(arr, 0, rotated, n - d, d);

        return rotated;
    }
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        int[] numbers = new int[n];
        
        // Fill initial array:
        for(int i = 0; i < n; i++){
            numbers[i] = scanner.nextInt();
        }
        scanner.close();
        
        // Rotate array by d elements:
        numbers = rotateArray(numbers, d);
        
        // Print array's elements as a single line of space-separated values:
        for(int i : numbers) {
            System.out.print(i + " ");
        }
        System.out.println();
    } 
        
}
*/