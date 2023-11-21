import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Arrays;

class Solution {
    public List<Integer> solution(String[] name, int[] yearning, String[][] photo) {
int[] answer = {};
        List<Integer> list = new ArrayList<>();
        
        int grade = 0;

        // 이름, 그리움 점수 map 만들기
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(int i=0; i<name.length; i++){
          map.put(name[i], yearning[i]);
        }
        
        for(int i=0; i<photo.length; i++) {
        	int sum = 0;
        	for(String person: name) {
        		for(int j=0; j<photo[i].length; j++) {
        			if(person.equals(photo[i][j])) {
        				grade = map.get(person);
        				System.out.println("grade" + grade);
        				sum += grade;
        				System.out.println("sum" + sum);
        			}
        		}

        	}
        	list.add(sum);	
        }
        
        
        return list;
    }
}