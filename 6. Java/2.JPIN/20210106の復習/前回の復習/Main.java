
public class Main {

	public static void main(String[] args) {
		// Listクラス（オーバーロード）
		List list = new List();
		list.add("A");
		list.add("B");
		list.add("C");

		for (int i = 0; i < list.size(); i++) {
			System.out.println(list.get(i));
		}
	}

}
