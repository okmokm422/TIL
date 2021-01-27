
public class Sample {

	public static void main(String[] args) {
		// staticフィールドを使う
		// インスタンスを作らなくても使える
		A.num = 10;
		System.out.println(A.num);
		// statißcメソッド
		A.hello();
		// インスタンスを新しく作る
		A a = new A();
		a.value = 10;
		a.test();
		// スタティックでもクラス.メンバー名でコンパイルエラーにならない
		a.num = 100;
		a.hello();

		int num = Integer.parseInt("100");
	}

}
