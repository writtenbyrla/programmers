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
        
        int sortIndex = Arrays.asList(arr).indexOf(sort_by);
        Arrays.sort(answer, Comparator.comparingInt(row -> row[sortIndex]));
        
        return answer;
    }
}