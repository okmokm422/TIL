
public class C {

	// throws SampleException3で、SampleException3の例外はthrowしても良いと明記
	public void test() throws SampleException3 {
		// SampleException3の例外クラスはthrowする
		throw new SampleException3();
	}
}
