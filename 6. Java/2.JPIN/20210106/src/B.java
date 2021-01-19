
public class B {

	public B(String name) {
		// コンストラクタ呼び出し
		// コンストラクタの定義はないけど、
		// コンパイルされるとコンパイラが引数なし処理なしのコンストラクタを勝手に追加する
		// デフォルトコンストラクタ
		System.out.println("Hello, " + name + "!");
	}

	public B() {
		System.out.println("hello2!");
	}
}