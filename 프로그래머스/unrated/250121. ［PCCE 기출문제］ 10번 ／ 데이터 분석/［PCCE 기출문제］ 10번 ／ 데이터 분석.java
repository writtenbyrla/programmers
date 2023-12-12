import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int count = 0;
        for(int i=0; i<data.length; i++){
            if(ext.equals("code")&&(data[i][0]<val_ext)){
                count++;
            }else if(ext.equals("date")&&(data[i][1]<val_ext)){
                count++;
            }else if(ext.equals("maximum")&&(data[i][2]<val_ext)){
                count++;
            }else if(ext.equals("remain")&&(data[i][3]<val_ext)){
                count++;
            }
        }
        
        int[][] answer = new int[count][4];
        int answerIndex = 0;
        for(int i=0; i<data.length; i++){
                if(ext.equals("code")&&(data[i][0]<val_ext)){
                    answer[answerIndex++] = Arrays.copyOf(data[i], data[i].length);
                }else if(ext.equals("date")&&(data[i][1]<val_ext)){
                    answer[answerIndex++] = Arrays.copyOf(data[i], data[i].length);
                }else if(ext.equals("maximum")&&(data[i][2]<val_ext)){
                    answer[answerIndex++] = Arrays.copyOf(data[i], data[i].length);
                }else if(ext.equals("remain")&&(data[i][3]<val_ext)){
                    answer[answerIndex++] = Arrays.copyOf(data[i], data[i].length);
                }
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