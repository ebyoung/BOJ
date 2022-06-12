import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] data = new int [N][2];
		for(int i = 0; i < N; i++) {
			int w = sc.nextInt();
			int h = sc.nextInt();
			data[i][0] = w;
			data[i][1] = h;
		}
		
		int[] rank = new int[N];
		
		for(int i = 0; i < N; i++) {
			int r = 1;
			for(int j = 0; j < N; j++) {
				if( i != j && data[i][0] < data[j][0] && data[i][1] < data[j][1] )
					r++;
			}
			System.out.printf("%d ", r);
		}
	}
}