
public class Order {

	private Item item;
	private int qty;

	// コンストラクタ生成
	// フィールドの後、メソッドの前に定義することが多い
	public Order(Item item, int qty) {
		super();
		this.item = item;
		this.qty = qty;
	}

	public Item getItem() {
		return item;
	}

	//	// コンストラクタを完璧にするためにset削る
	//	public void setItem(Item item) {
	//		this.item = item;
	//	}

	public int getQty() {
		return qty;
	}

	// コンストラクタを完璧にするためにset削る
	//	public void setQty(int qty) {
	//		this.qty = qty;
	//	}

	public int getTotal() {
		return item.getPrice() * this.qty;
	}

}
