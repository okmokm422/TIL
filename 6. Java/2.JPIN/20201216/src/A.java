
//　使われる側のプログラム

public class A {
	// アクセス修飾子であるpublic/publicでフィールドを非公開/公開にする
	// フィールドを選択→右クリックでgetter, setterを作れる
	public String name; // フィールド（Java用語）：属性（OO用語）

	public String getName() {
		return name; // 　メソッドの中で宣言=ローカル変数
	}

	public void setName(String name) {
		this.name = name; // thisがついている　→　自分自身のインスタンスで宣言
	}

	// メソッド
	// staticはなし
	public void sayHello() {
		System.out.println("Hello, I'm " + name + "!");
	}
}
