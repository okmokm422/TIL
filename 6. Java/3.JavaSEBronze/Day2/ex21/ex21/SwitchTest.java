package ex21;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SwitchTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		switch (a) {
		case 1:
			System.out.println("one");
			break;
		case 2:
			System.out.println("two");
			break;
		default:
			System.out.println("other");
			break;
		}
	}

}
