package ex1;

public class ArrayTest {

	public static void main(String[] args) {
		int[] array = new int[3];
		array[0] = 10;
		array[1] = 20;
		array[2] = 30;

		for (int i = 0; i < 3; i++) {
			int val = array[i];
			System.out.println(val);
		}
	}

}
