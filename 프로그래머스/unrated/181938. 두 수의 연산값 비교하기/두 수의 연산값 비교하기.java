class Solution {
    public int solution(int a, int b) {
        
        String str = "" + a + b;
        int str2 = Integer.parseInt(str);
        int num = 2 * a * b;
        
        
        return str2 >= num ? str2 : num ;
    }
}