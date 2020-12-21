package ex21;

public class MethodTest {

	public static void main(String[] args) {
		int val = returnableValue();
		System.out.println(val);

	}

	public static int returnableValue() {
		int tmp = 100;
		return tmp;
	}
}
