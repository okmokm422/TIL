
public class B {

	// 例外はスーパークラスで処理するためにthrowする
	public void test() throws SampleException3 {
		new C().test();
	}
}
