
public class Order {

	public Item item;
	public int qty;

	public int getTotal() {
		int result = item.getPrice() * qty;
		return result;
	}

	public Item getItem() {
		return item;
	}

	public void setItem(Item item) {
		this.item = item;
	}

	public int getQty() {
		return qty;
	}

	public void setQty(int qty) {
		this.qty = qty;
	}

}
