package com.sample;

// インターフェイスは以下を意識している
// インスタンス化を不用意にされないようにする
// （型情報だけのクラスがある）
// 継承したときにオーバーライドしたいものは確実にされるように
// 型情報だけで中身は実装したくないもの　→　return nullなど無理やり書かないといけない

public class D implements A {
	public void hello() {
		System.out.println("D");
	}
}
