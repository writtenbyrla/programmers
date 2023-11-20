import java.util.Map;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i=0; i<players.length; i++) {
        	map.put(players[i], i);
        }

        for (String player : callings){
        	int index = map.get(player);
            
            String frontPlayer = players[index-1];
            
            map.replace(frontPlayer, index);
            players[index] = frontPlayer;
            
            map.replace(player, index-1);
            players[index-1] = player;
        }   
        return players;
    }
}