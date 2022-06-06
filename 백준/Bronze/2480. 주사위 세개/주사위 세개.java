import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int num3 = sc.nextInt();
		
		if (num1 == num2 && num1 == num3 && num2 == num3)
			System.out.println(10000 + num1 * 1000);
		else if (num1 == num2 || num1 == num3)
			System.out.println(1000 + num1 * 100);
		else if (num2 == num3)
			System.out.println(1000 + num2 * 100);
		else {
			int maxVal = num1 > num2 ? num1 : num2;
			maxVal = maxVal > num3 ? maxVal : num3;
			System.out.println(maxVal * 100);
		}
	}
}