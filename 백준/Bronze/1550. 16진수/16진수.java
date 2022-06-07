import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String hexadecimal = sc.next();
		int number = 0;
		
		for (int i = 0; i < hexadecimal.length(); i++) {
			int a = hexadecimal.charAt(i);
			double p = Math.pow(16, hexadecimal.length() - i - 1);
			if (a < 58)
				number += (a - 48) * p;
			else
				number += (a - 55) * p;
		}
		
		System.out.println(number);
	}
}