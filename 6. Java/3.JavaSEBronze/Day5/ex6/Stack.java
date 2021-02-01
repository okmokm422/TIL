
public class Stack {
	private int[] vals = new int[10];
	private int index = 0;

	public void push(int val) {
		this.vals[index] = val;
		index++;
	}

	public int pop() {
		index--;
		return vals[index];
	}
}
