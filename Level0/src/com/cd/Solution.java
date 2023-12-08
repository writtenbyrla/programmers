package com.cd;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Solution s = new Solution();

//		s.solution4("aaaaa", "bbbbb");
		s.solution5(7, 3);

	}
	
	// 대소문자 바꾸기
	 public String[] solution1() {
			Scanner sc = new Scanner(System.in);
			String a = sc.next();
			
			char[] array = a.toCharArray();
			for(int i=0; i<array.length; i++) {
				if(Character.isUpperCase(array[i])) {
					System.out.print(Character.toLowerCase(array[i]));
				} else {
					System.out.print(Character.toUpperCase(array[i]));
				}
			}
			return null;
	    }
	
	
    public String[] solution2() {
    	
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for(int i=0; i<a.length(); i++){
            System.out.println(a.charAt(i));
        }
        
        return null;
    }
    
    public String solution3(String my_string, String overwrite_string, int s){

    	String my_string2 = "";
    	String text1 = my_string.substring(0, s);
    	
    	String text2 = my_string.substring(s+overwrite_string.length(), my_string.length());
       
    	my_string2 = text1 + overwrite_string + text2; 
    	
        return my_string2;
    } 
    
    public String solution4(String str1, String str2){

    	String answer = "";
        
        for(int i=0; i<str1.length()-1; i++){
        	answer += str1.substring(i,i+1) + str2.substring(i, i+1);
            
        }
        System.out.println(answer);
    	
        return answer;
    }

    public int solution5(int num1, int num2) {
    	float f = (float)num1 / (float)num2 * 1000;
    	System.out.println((int)f);
        return (int)f;
    }
    
    public int solution6(int n) {
        int sum = 0;
        for(int i=2; i<=n; i= i+2){
            sum += i;
        }
        return sum;
    }
    
    
}
