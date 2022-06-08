import java.util.Scanner;

public class Main {
	
	static int N;
	static int[] dp = new int[5001];
	static int answer = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		for(int i = 0; i < 5; i++) {
			if( i != 3 )
				dp[i] = 5001;
		}
		dp[3] = 1;
		dp[5] = 1;
		sugar(N);
		if( dp[N] > 5000 )
			System.out.println(-1);
		else System.out.println(dp[N]);

	}
	
	static int sugar(int n) {
		if( dp[n] == 0 ) {
			dp[n] = Math.min(sugar(n-3), sugar(n-5)) + 1;			
		}
		return dp[n];
	}
}