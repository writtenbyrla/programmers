package com.cd;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

	public static void main(String[] args) {
		Solution s = new Solution();
		String[] name = {"may", "kein", "kain", "radi"};
		int[] yearning = {5, 10, 1, 3};
		String[][] photo = {{"may", "kein", "kain", "radi"},{"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};
		//s.solution4(name, yearning, photo);
		s.solution5(10);
		s.solution6(-4, 2);
	}
	
	// 경주 달리기
	// 시간 초과
	public String[] solution() {
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
	public String[] solution2() {
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
	public String[] solution3() {
	        
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

	// 추억 점수
    public List<Integer> solution4(String[] name, int[] yearning, String[][] photo) {
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
	    
    public int solution5(int n) {

        int answer = 0;
        for(int i=1; i<=n; i++){
        	if(n%i == 1) {
        		answer = i;
        		break;
        	}
   
        }
        
        return answer;

    }
   
    public long[] solution6(int x, int n) {
        long[] answer = new long[n];
        
        for(int i=1; i<=n; i++){
            answer[i-1] = x*i;
        }
        
        return answer;
    }

    
}
