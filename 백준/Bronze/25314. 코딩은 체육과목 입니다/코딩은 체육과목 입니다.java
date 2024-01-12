import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int number = Integer.parseInt(sc.nextLine());
		int number2 = number/4;

		for(int i=0; i<number2 ; i++) {
			System.out.print("long ");
		}
		System.out.println("int");
	}
}