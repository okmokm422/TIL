package ex11;

public class ThreeMethodTest {

	public static void main(String[] args) {
		System.out.println("A");
		test();
	}

	public static void test() {
		System.out.println("B");
		sample();
	}

	public static void sample() {
		System.out.println("C");
	}
}
