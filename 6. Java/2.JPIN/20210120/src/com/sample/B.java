package com.sample;

// Aを拡張したクラス
public class B extends A {
	private int num;

	// 承継元にはsetterがあるが、承継先のBにはgetterしかない
	public int getNum() {
		return num;
	}

}
