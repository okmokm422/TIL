
public class List {

	private String value;
	private int index;
	private List next; // 再帰関連

	// コンストラクタ（オーバーロード）（公開）
	public List() {
		this.value = null;
		this.index = 0;
		this.next = null;
	}

	// コンストラクタ（オーバーロード）（非公開）
	private List(int index) {
		this(); // オーバーロードされている引数なしのコンストラクタを呼び出す
		this.index = index;
	}

	public void add(String value) {
		if (this.value == null) {
			this.value = value;
			return; // addメソッドを呼び出した側に制御を戻す
		}
		if (this.next == null) {
			this.next = new List(this.index + 1); // コンストラクタ呼び出し
		}
		// 自分自身のaddメソッド呼び出し
		this.next.add(value);
	}

	public String get(int index) {
		if (this.index == index) {
			return this.value;
		}
		if (this.next == null) {
			return null;
		}
		return this.next.get(index);
	}

	public int size() {
		if (this.next == null) {
			return this.index + 1;
		}
		return this.next.size();
	}
}
