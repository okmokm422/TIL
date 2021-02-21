
public class A {
	public void hello() {
		System.out.println("Hello");
	}

	public static void main(String[] args) throws TestExeption {
		try {
			new B().test();
		} catch (SampleException3 e) {
			// TestExceptionの例外をthrowする
			throw new TestExeption();
		}

	}
}
