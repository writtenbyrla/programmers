package com.cd;

public class Solution2 {

	public static void main(String[] args) {
		Solution2 s = new Solution2();
//		s.solution(123);
		s.solution2("pPooooyY");
		s.solution3("2three45sixseven");
	}
	
	 public int solution(int n) {
	        int answer = 0;

	        String str = Integer.toString(n);
	        
	        for(int i=0; i<str.length(); i++){
	            answer += str.charAt(i)-'0';
	        }
	        
	        return answer;
	    }
	 
	 boolean solution2(String s) {
	        boolean answer = true;
	        
	        int num = 0;
	        int num2 = 0;
	        
	        for(int i=0; i<s.length(); i++){
	        	if(s.charAt(i)=='p' || s.charAt(i)=='P') {
	        		num++;
	        	} else if(s.charAt(i)=='y' || s.charAt(i) =='Y'){
	        		num2++;
	        	}
	        }

	        return num==num2;
	    }
	    
	 public int solution3(String s) {
		 int answer = 0;

		 String[] arr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

		 
		 for(int i=0; i<arr.length; i++) {
			 if(s.contains(arr[i])) {
				s = s.replace(arr[i], Integer.toString(i));
			 }
		 }
		 
		 answer = Integer.parseInt(s);
	        
		 return answer;
	 }
}
