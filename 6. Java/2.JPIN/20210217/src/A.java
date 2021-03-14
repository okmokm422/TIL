
public class A {
	private int num;

	public A(int num) {
		this.num = num;
	}

	// equalsメソッドを自動生成
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		A other = (A) obj;
		if (num != other.num)
			return false;
		return true;
	}

}
