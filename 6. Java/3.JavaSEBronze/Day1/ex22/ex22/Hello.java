package ex22;

public class Hello {

	public static void main(String[] args) {
		int a = 10;
		int b = ++a;
		int c = 10;
		int d = c++;
		// 変数aの値に+1された後、その値がbに代入される
		System.out.println("a: " + a);
		System.out.println("10に前置インクリメントした値は" + b);
		// 変数ｃの値がdにコピーされた後、cに+1される
		System.out.println("c: " + c);
		System.out.println("10に後置インクリメントした値は" + d);

	}

}
