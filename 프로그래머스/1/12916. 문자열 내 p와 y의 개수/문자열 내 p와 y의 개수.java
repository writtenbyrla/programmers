class Solution {
    boolean solution(String s) {
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
}