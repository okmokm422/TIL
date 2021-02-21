import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sample2 {
	// throws Exceptionをつけないと、コンパイルエラーになる
	// デフォルトでJavaは検査例外なのに、BufferedReaderで例外をスルーする
	// https://docs.oracle.com/javase/jp/11/docs/api/java.base/java/io/BufferedReader.html#readLine()
	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(
				new InputStreamReader(System.in));

		String line = null;
		int total = 0;

		System.out.print("> ");

		try {
			while ((line = in.readLine()) != null) {
				try {
					int input = Integer.parseInt(line);
					if (input == 0) {
						break;
					}
					total += input;
					System.out.println(total);
				} catch (NumberFormatException e) {
					System.out.println("invalid number");
				}
				System.out.print("> ");

			}
		} catch (IOException e) {
			System.out.println("invalid number");
		}
	}
}
