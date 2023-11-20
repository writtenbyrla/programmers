package com.cd;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Solution s = new Solution();
//		s.solution1();
		s.solution4();

	}
	
	// 대소문자 바꾸기
	 public String[] solution1() {
			Scanner sc = new Scanner(System.in);
			String a = sc.next();
			
			char[] array = a.toCharArray();
			for(int i=0; i<array.length; i++) {
				if(Character.isUpperCase(array[i])) {
					System.out.print(Character.toLowerCase(array[i]));
				} else {
					System.out.print(Character.toUpperCase(array[i]));
				}
			}
			return null;
	    }
	
	// 경주 달리기
	// 시간 초과
    public String[] solution2() {
        String[] answer = {};
        
        String[] players = {"mumu", "soe", "poe", "kai", "mine"};
        String[] callings = {"kai", "kai", "mine", "mine"};

        String temp = "";
        for(int i=0; i<callings.length; i++){
        	for(int j=0; j<players.length; j++) {
        		if(callings[i].equals(players[j])) {
        			temp = players[j-1];
        	        players[j-1] = players[j];
        			players[j]=temp;
        		};
        	}

        }
        System.out.println(Arrays.toString(players));
        
        return answer;
    }

    // 시간 초과
    public String[] solution3() {
        String[] answer = {};
        
        String[] players = {"mumu", "soe", "poe", "kai", "mine"};
        String[] callings = {"kai", "kai", "mine", "mine"};
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        List<String> list = new ArrayList<>(Arrays.asList(players));
        
        for(int i=0; i<players.length; i++) {
        	map.put(players[i], i);
        	
        }
        System.out.println(map);

        for(int i=0; i<callings.length; i++){
        	System.out.println(map);
        	int index = map.get(callings[i]);
            System.out.println(index);
            list.remove(index);
            list.add(index-1, callings[i]);
            map.remove(callings[i]);
            map.put(callings[i], index-1);
            System.out.println(list);
        }
   
        return answer;
    }
    
    // 시간 초과 => 향상된 for문으로 수정하니까 통과
    public String[] solution4() {
        
        String[] players = {"mumu", "soe", "poe", "kai", "mine"};
        String[] callings = {"kai", "kai", "mine", "mine"};
        
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i=0; i<players.length; i++) {
        	map.put(players[i], i);
        	
        }
        System.out.println(map);

        for(int i=0; i<callings.length; i++){
        	int index = map.get(callings[i]);
            System.out.println(index);
            
            String frontPlayer = players[index-1];
            System.out.println(frontPlayer);
            
            map.replace(frontPlayer, index);
            players[index] = frontPlayer;
            
            map.replace(callings[i], index-1);
            players[index-1] = callings[i];

        }

        return players;
    }


}
