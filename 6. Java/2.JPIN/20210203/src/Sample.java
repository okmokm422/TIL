
public class Sample {

	public static void main(String[] args) {
		A a = Factory.create();
		Display d = new Display();
		d.show(a);
	}

}