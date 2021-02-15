package com.sample;

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		B b = new B();
		b.test();
		b.setNum(100);
		System.out.println(b.getNum());

		// B2のインスタンスを生成するとき、A2とB2のどちらのコンストラクタが表示されるか？
		// →B2のコンストラクタが呼び出されているのに先にA2と表示されている
		B2 b2 = new B2();

		// スーパークラスとサブクラス両方動くことを確認
		B3 b3 = new B3();
		b3.hello();
		b3.bye();
	}

}
