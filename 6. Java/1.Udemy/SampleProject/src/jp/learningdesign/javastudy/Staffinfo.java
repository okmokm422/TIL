package jp.learningdesign.javastudy;


class Staff {
	// フィールド名
	String name;
	int staffid;
	String email;

	public void sayhello() {
		System.out.println("Hello " + this.name);
	}
}

public class Staffinfo {

	public static void main(String[] args) {
		// classを呼び出して使う
		Staff yamada = new Staff(); // yamadaさんの情報を格納するインスタンスを宣言
		yamada.name = "Taro Yamada";

		// System.out.println(yamada.name);
		yamada.sayhello();
	}

}
