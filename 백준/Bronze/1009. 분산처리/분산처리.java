import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = 1;
			for (int j = 0; j < b; j++) {
				c = (c * a) % 10;
			}
			if (c != 0) {
				System.out.println(c);				
			} else {
				System.out.println(10);
			}
		}
	}
}
