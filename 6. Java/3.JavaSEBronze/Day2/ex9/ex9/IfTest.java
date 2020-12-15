package ex9;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class IfTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int score = Integer.parseInt(br.readLine());
		if (0 <= score & score <= 100) {
			System.out.println("範囲内です。");
		} else {
			System.out.println("範囲外です。");
		}
	}

}
