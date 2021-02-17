import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Sample2 {

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(
				new InputStreamReader(System.in));

		String line = null;
		int total = 0;

		System.out.print("> ");

		while ((line = in.readLine()) != null) {

			total += Integer.parseInt(line);
			System.out.println(total);
			System.out.print("> ");
		}
	}
}
