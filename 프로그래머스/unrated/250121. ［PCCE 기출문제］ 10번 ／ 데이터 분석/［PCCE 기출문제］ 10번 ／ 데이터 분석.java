import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        String[] arr = {"code", "date", "maximum", "remain"};
        int index = 0;
        for(int i=0; i<arr.length; i++){
            if(ext.equals(arr[i])){
                index = i ;
            }
        }
        
        List<int[]> list = new ArrayList<>();
        for(int i=0; i<data.length; i++){
            if(data[i][index]<val_ext){
                list.add(data[i]);
            }
        }    
            
        int[][] answer = new int[list.size()][4];
        for(int i=0; i<answer.length; i++){
            answer[i] = list.get(i);
        }

        if(sort_by.equals("code")){
            Arrays.sort(answer, Comparator.comparingInt(row -> row[0]));      
        }else if(sort_by.equals("date")){
            Arrays.sort(answer, Comparator.comparingInt(row -> row[1]));
        }else if(sort_by.equals("maximum")){
            Arrays.sort(answer, Comparator.comparingInt(row -> row[2]));
        }else if(sort_by.equals("remain")){
            Arrays.sort(answer, Comparator.comparingInt(row -> row[3]));
        }

        return answer;
    }
}