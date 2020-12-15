package ex14;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class IfTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		if (10 < a)
			System.out.println("大きい");

	}

}
