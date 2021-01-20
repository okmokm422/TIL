
public class Hoge {

	public static int num; // フィールド宣言

	// インスタンスを生成しないと動かない
	public void hello1() {
		System.out.println("Hello");
	}

	// インスタンスを生成しなくても動く
	public static void hello2() {
		System.out.println("Static Hello");
	}

}
