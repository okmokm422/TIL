// パッケージに属するクラスはパッケージ名が先頭に表示される
package com.sample;

public class A {
	public void test() {
		System.out.println("com.sample.A.test()だよ");
	}

	// int型のnumを宣言
	private int num;

	// numにsetterのみを作成
	public void setNum(int num) {
		this.num = num;
	}

}