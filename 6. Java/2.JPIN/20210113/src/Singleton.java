
public class Singleton {

	// フィールド
	// Singleton型のinstance
	// staticにコピーされるもの
	private static Singleton instance;
	private String value;

	// 引数なしのコンストラクタを明示的に書く→勝手にデフォルトコンストラクタはつくられない
	//　コンストラクタをprivateにする→外部クラスからnewでインスタンス作成できない
	private Singleton() {
	}

	// privateコンストラクタで、インスタンスを取り出すためのメソッド
	// staticなのでインスタンスを作らなくても良い
	public static Singleton getInstance() {
		if (instance == null) {
			// 同じクラス内でインスタンス作成
			instance = new Singleton();
		}
		return instance;
	}

	//　valueのsetter, getter
	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}

}
