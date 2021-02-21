
public class UseTest {

	public static void main(String[] args) {

		Test t = new Test();

		try {
			t.execute(-1);
			System.out.println("safe");
		} catch (SampleException e) {
			System.out.println("unsafe");
		}

		try {
			t.execute(1);
			System.out.println("safe");
		} catch (SampleException e) {
			System.out.println("unsafe");
		}
	}
}