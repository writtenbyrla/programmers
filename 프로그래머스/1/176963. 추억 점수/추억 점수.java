import java.util.*;

class Solution {
    public List<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        
        List<Integer> list = new ArrayList<>();
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(int i=0; i<name.length; i++){
          map.put(name[i], yearning[i]);
        }
        
        for(int i=0; i<photo.length; i++) {
        	int sum = 0;
        	for(String person: name) {
        		for(int j=0; j<photo[i].length; j++) {
        			if(person.equals(photo[i][j])) {
        				sum += map.get(person);
        			}
        		}
        	}
        	list.add(sum);	
        }  
        return list;
    }
}