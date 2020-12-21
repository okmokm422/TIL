package ex12;

public class ThreeMethodTest {

	public static void main(String[] args) {
		System.out.println("A");
		test();
		System.out.println("E");
	}

	public static void test() {
		System.out.println("B");
		sample();
		System.out.println("D");
	}

	public static void sample() {
		System.out.println("C");
	}

}
