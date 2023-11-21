class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        
        double count = 0;
        for(int item : arr){
            count += item;
        }
        
        answer = count/arr.length;
        
        return answer;
    }
}