package ex4;

public class Robot {
	// privateフィールドにする
	private String name;

	public void sayHello() {
		System.out.println("Hi, I'm " + name);
	}

	// nameの値を取り出すゲッター
	public String getName() {
		return name;
	}

	// nameの値をセットするセッター
	public void setName(String name) {
		this.name = name;
	}

}
