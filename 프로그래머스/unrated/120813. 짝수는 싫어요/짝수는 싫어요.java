class Solution {
    public int[] solution(int n) {
  
        int[] answer = {};
        
        if(n%2 == 0){
            answer = new int[n/2];
        } else {
            answer = new int[n/2+1];
        }
       
        int count = 0;
        
        for(int i=1; i<=n; i++){
            if(i%2!=0) {answer[count]=i; count++;}
        }
        
        
        

        return answer;
    }
}