package ex18;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class IfTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		if (100 < a)
			System.out.println("エラー");
		else if (a < 0)
			System.out.println("エラー");
		else if (10 < a)
			System.out.println("大きい");
		else
			System.out.println("小さい");
	}

}
