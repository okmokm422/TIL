package com.test;

import com.sample.A; // 完全修飾クラス名で書くと長いので、import分を使う
// import com.sample.test.A; // コンパイルエラーになる 名前が重複しておりどのパッケージなのか判断できないから→完全修飾クラス名で

public class Main {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ
		com.sample.A a = new com.sample.A(); // 完全修飾クラス名で書く
		a.test();

		A a2 = new A(); // import文を利用
		a2.test();

		com.sample.test.A a3 = new com.sample.test.A(); // importできない場合は完全修飾クラス名を使うしかない
		a3.test();
	}
}