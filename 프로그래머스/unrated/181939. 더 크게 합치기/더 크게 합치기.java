class Solution {
    public int solution(int a, int b) {
        String str1 = Integer.toString(a).concat(Integer.toString(b));
        String str2 = Integer.toString(b).concat(Integer.toString(a));
        
        int answer1 = Integer.parseInt(str1);
        int answer2 = Integer.parseInt(str2);
        
        return answer1>=answer2? answer1 : answer2;
    }
}