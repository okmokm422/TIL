
public class Hello {

	public static void main(String[] args) {

		// 1. 加算演算子で文字列をつなげる
		System.out.println("abc" + "def");
		System.out.println("abc" + 1 + 2);
		System.out.println(1 + 2 + "yen");

		// 2. char型の文字をint型に変換できることを確認

		// 3. 同ファイルからメソッドを参照
		test();

		// 4. 外部プログラムのメソッドを参照
		Test.execute();

		// 5. 標準クラスライブラリ
		// 基本ライブラリ：https://docs.oracle.com/javase/jp/11/docs/api/java.base/java/lang/package-summary.html
		int num = Integer.parseInt("100"); // Integerクラス 文字列を数字に変換
		System.out.println(num * 2);

		// 6. オブジェクト指向
		// class Aを使う
		A a = new A(); // インスタンス生成
		a.setName("Java");
		a.sayHello(); // 
		System.out.println("ハッシュ値? " + a);
		// System.out.println(a)で表示する値は、ObjectクラスのtoString()で表示しているハッシュ値？

		A b = new A();
		b.setName("Hoge");
		b.sayHello();

		A c = a;
		c.sayHello();

	}

	public static void test() {
		System.out.println("test");
	}

}
