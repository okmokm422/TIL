package ex16;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class IfTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		if (a < 10)
			System.out.println("大きい");
		System.out.println("常に実行される");

	}

}
