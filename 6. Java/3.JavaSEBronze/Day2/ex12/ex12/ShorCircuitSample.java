// ショートサーキット演算子

package ex12;

public class ShorCircuitSample {

	public static void main(String[] args) {
		int a = 1;
		int i = 4;
		if (a == 1 || i++ < 5) {
			// do something
		}
		System.out.println(i);

	}

}
