package com.test;

// abstractで抽象クラスにする
public abstract class E implements A {
	@Override
	public void bye() {
		System.out.println("bye");
	}

	// 中身がないメソッド　中括弧をつけない
	public abstract void test();
}
