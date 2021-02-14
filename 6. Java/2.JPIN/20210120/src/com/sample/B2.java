package com.sample;

public class B2 extends A2 {

	public B2() {
		// サブクラスにsuper();がコンパイル時に勝手に追加されている
		// super();
		System.out.println("B2");
	}
}
