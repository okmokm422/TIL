package ex6;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ArrayTest {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] allScore = new int[3];
		for (int i = 0; i < allScore.length; i++) {
			int inputScore = Integer.parseInt(br.readLine());
			allScore[i] = inputScore;
		}
		int total = 0;
		for (int i = 0; i < allScore.length; i++) {
			total = total + allScore[i];
		}

		int average = total / allScore.length;
		System.out.println(average);

	}

}
