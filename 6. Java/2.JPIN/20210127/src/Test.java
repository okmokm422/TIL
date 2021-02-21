// 例外を起こして

public class Test {
	// Throws 例外名 でどんな例外をスルーするのか書く

	// コンパイラは宣言の部分（throws ~Exception）を見てどんなtry catchが必要なのかを判断する
	public void execute(int value) throws SampleException {
		if (value < 0) {
			throw new SampleException();

			// 以下の書き方もできるが変数に入れる必要性がない
			//			SampleException ex = new SampleException();
			//			throw ex;
		}
	}

	public void execute2(int value2) {
		if (value2 == 0) {
			new SampleException2(); // throw書かなくても良い
		}
	}

}
