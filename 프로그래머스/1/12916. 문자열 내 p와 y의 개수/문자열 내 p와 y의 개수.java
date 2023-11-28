class Solution {
    boolean solution(String s) {
        boolean answer = true;
        char[] arr = s.toCharArray();
        int num = 0;
        int num2 = 0;
        
	        for(int i=0; i<arr.length; i++){
	        	if(arr[i]=='p' || arr[i]=='P') {
	        		num++;
	        	} else if(arr[i]=='y' || arr[i] =='Y'){
	        		num2++;
	        	}
	        }
        
        if(num == num2){
            answer = true;
        } else {
            answer = false;
        }

        return answer;
    }
}