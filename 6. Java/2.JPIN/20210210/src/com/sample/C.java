package com.sample;

// アクセス修飾辞なしのクラス
class C implements A {
	@Override
	public void hello() {
		System.out.println("C");
	}

}