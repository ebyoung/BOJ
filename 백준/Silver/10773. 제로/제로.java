import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Stack<Integer> stack = new Stack();
		
		for(int i = 0; i < N; i++) {
			int num = sc.nextInt();
			if( num == 0 )
				stack.pop();
			else
				stack.push(num);
		}
		int total = 0;
		while(!stack.empty()) {
			total += stack.pop();
		}
		System.out.println(total);
	}
}