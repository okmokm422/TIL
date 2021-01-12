
public class Sample {

	public static void main(String[] args) {

		// 1. 参照について
		int[] array = new int[3];
		array[0] = 10;
		array[1] = 20;
		array[2] = 30;

		int[] array2 = array;
		array2[0] = 100; // 参照なので、arrayも更新される

		for (int i : array) {
			System.out.println(i);
		}

		// 2.配列の要素に要素に値が入っていない
		A[] array3 = new A[3];

		for (A a : array3) {
			System.out.println(a);
		}

		// 3.配列の要素に要素に値を入れる
		A[] array4 = new A[3];
		array4[0] = new A(); // インスタンスを生成して配列の要素に代入＝ヒープの確保
		array4[1] = new A();
		array4[2] = new A();

		for (A a : array4) {
			System.out.println(a);
		}

		// 4.Orderクラス, Itemクラス, ShoppingCartクラスを使ってメインメソッドを実装

		// Itemクラス
		Item apple = new Item();
		apple.setName("apple");
		apple.setPrice(100);

		Item banana = new Item();
		banana.setName("banana");
		banana.setPrice(80);

		Item orange = new Item();
		orange.setName("orange");
		orange.setPrice(120);

		// Orderクラス
		Order o1 = new Order();
		o1.setItem(apple);
		o1.setQty(3);

		Order o2 = new Order();
		o2.setItem(banana);
		o2.setQty(5);

		Order o3 = new Order();
		o3.setItem(orange);
		o3.setQty(2);

		// ShoppingCartクラス
		ShoppingCart cart = new ShoppingCart();
		cart.add(o1);
		cart.add(o2);
		cart.add(o3);

		int total = cart.getTotal();
		System.out.println(total);
	}

}
