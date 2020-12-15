package ex21;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class WhileLoopSample {

	public static void main(String[] args) throws Exception {
		// TODO 自動生成されたメソッド・スタブ
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		while (a - 1 > 0) {
			System.out.print("*");
			a--;
			if (a - 1 < 0) {
				break;
			}
		}

	}

}
