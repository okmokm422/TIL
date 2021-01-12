
public class ShoppingCart {

	//  10個の要素を持つorders配列を生成
	private Order[] orders = new Order[10];
	// index初期化
	private int index = 0;

	// Order型のorderを引数に受け、orders配列のindex番目にorderを追加する
	public void add(Order order) {
		orders[index] = order;
		index++;
	}

	public int getTotal() {
		int total = 0;
		for (int i = 0; i < index; i++) {
			total += orders[i].getTotal(); // totalにordersのi番目のgetTotalを加算
		}
		return total;
	}

}
