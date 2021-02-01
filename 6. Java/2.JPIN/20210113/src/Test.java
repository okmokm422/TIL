
public class Test {

	private int num;

	public static void execute() {
		// インスタンスを生成しないとnumにはアクセスできない
		Test test = new Test();
		System.out.println(test.num);
	}

}
