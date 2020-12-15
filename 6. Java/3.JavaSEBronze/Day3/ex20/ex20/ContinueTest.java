package ex20;

public class ContinueTest {

	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			System.out.print(i);
			if (8 < i) {
				continue;
			}
			System.out.print(",");
		}
	}

}
