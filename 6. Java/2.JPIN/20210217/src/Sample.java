
public class Sample {

	public static void main(String[] args) {
		A a = new A(100);
		A b = new A(100);

		System.out.println(a == b);
		System.out.println(a.equals(b)); // なぜFalse？

		Item a2 = new Item(100, "apple");
		Item b2 = new Item(100, "banana");
		System.out.println(a2.equals(b2));

		String a3 = "hoge";
		String b3 = "hoge";
		System.out.println(a3 == b3);
		System.out.println(a3.equals(b3));

		String a4 = new String("hoge");
		String b4 = "hoge";
		System.out.println(a4 == b4);
		System.out.println(a4.equals(b4));

		Template t = new Hello();
		t.execute();
	}

}
