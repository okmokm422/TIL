package ex13;

public class ShortCircuitSample {

	public static void main(String[] args) {
		int a = 1;
		int i = 4;
		i++;
		if (a == 1 || i < 5) {
		}
		System.out.println(i);

	}

}
