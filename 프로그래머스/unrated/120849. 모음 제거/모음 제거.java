class Solution {
    public String solution(String my_string) {
        
        String[] arr = {"a", "e", "i", "o", "u"};

        for(String item : arr){
            my_string = my_string.replace(item, "");
        }
        
        
        return my_string;
    }
}