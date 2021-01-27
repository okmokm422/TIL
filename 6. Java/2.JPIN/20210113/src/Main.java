
public class Main {
	public static void main(String[] args) {

		Singleton a = Singleton.getInstance();
		Singleton b = Singleton.getInstance();

		a.setValue("Hello");
		System.out.println(b.getValue());
	}
}
