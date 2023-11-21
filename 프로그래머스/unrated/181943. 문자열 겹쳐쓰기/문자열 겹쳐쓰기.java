class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        
    	String my_string2 = "";
    	String text1 = my_string.substring(0, s);
    	
    	String text2 = my_string.substring(s+overwrite_string.length(), my_string.length());
       
    	my_string2 = text1 + overwrite_string + text2; 
    	
        return my_string2;
    }
}