import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        char[] array = a.toCharArray();
        for(int i=0; i<array.length; i++){
            if(Character.isUpperCase(array[i])){
                System.out.print(Character.toLowerCase(array[i]));
            } else {
                System.out.print(Character.toUpperCase(array[i]));
            }
        };
        
    }
}