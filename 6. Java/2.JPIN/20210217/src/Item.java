public class Item {
	private int id;
	private String name;

	public Item(int id, String name) {
		super();
		this.id = id;
		this.name = name;
	}

	@Override
	public boolean equals(Object obj) {

		// objがnullではない
		if (obj == null) {
			return false;
		}

		// objがItemではない
		if (obj instanceof Item == false) {
			return false;
		}

		// objがItem型であることが確認できたので…

		Item target = (Item) obj; // ダウンキャスト
		return this.id == target.id;
		// nameは比較していない。idだけを比較する。
	}

}
