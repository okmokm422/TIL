package com.sample;

public class B3 extends A3 {

	// 継承するけど一部のメソッドは引き継ぎたくないときはスーパークラスをOverRideする
	@Override
	public void hello() {
		System.out.println("hi");
		super.hello();
	}

	public void bye() {
		System.out.println("bye");
	}

}
