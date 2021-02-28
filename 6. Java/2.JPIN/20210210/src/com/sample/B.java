package com.sample;

// 非公開が標準
// publicがついていた場合、他のクラス内で直接インスタンスを作成することが可能
class B implements A {

	@Override
	public void hello() {

		System.out.println("B");
	}

}
