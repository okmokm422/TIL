
public class Item {

	private String name;
	private int price;

	// コンストラクタ追加
	public Item(String name, int price) {
		super();
		this.name = name;
		this.price = price;
	}

	// get と set
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

}
