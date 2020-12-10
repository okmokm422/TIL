public class Sample {

	public static void main(String[] args) {
		// TODO 自動生成されたメソッド・スタブ

		// 1. 大きい型を小さい型に入れられない
		long a1 = 10;
		// int b = a; エラー
		long b1 = a1;
		System.out.println(b1);

		// 2. キャスト式
		long a2 = 10;
		int b2 = (int) a2;
		System.out.println("a2の値は" + a2);
		System.out.println("b2の値は" + b2);

		// 3. longとintの計算
		int a3 = 10;
		long b3 = 10;
		long c3 = a3 + b3; // longとintの演算はlong同士の演算として扱われる
		int d3 = a3 + (int) b3; // キャストしてみるとどうか？
		System.out.println("型をlongにしたときのa3+b3の値は" + c3);
		System.out.println("元の値をキャストしたときのa3+b3の値は" + d3);

		// 4. 条件式
		int a4 = 9;
		if (a4 < 10) {
			System.out.println("small");
		} else if (a4 < 100) {
			System.out.println("medium");
		} else {
			System.out.println("big");
		}

		// 5. 課題
		// テストの点数が0より小さい→小、100より大→大きいを出すプログラム
		// Scanner scanner = new Scanner(System.in);
		// int score = scanner.nextInt();
		int score = 100;
		if (score < 0) {
			System.out.println("テストの点数は" + score + "点です。" + "too small!");
		} else if (score > 100) {
			System.out.println("テストの点数は" + score + "点です。" + "too big!");
		} else {
			System.out.println("テストの点数は" + score + "点です。");
		}

		// 答え
		if (score <= 100 && score <= 100) {
			System.out.println("正常");
		} else {
			System.out.println("以上");
		}

		// 6. switch文
		int a6 = 30;
		switch (a6) {
		case 10: // a6の値が10だったら以降実行（フォールスルー）
			System.out.println("a");
			break;
		case 20:
			System.out.println("b");
			break;
		case 30:
			System.out.println("c");
			break;
		default:
			System.out.println("d");
		}

		// 7. 繰り返し文
		for (int i = 1; i < 10; i += 2) {
			System.out.println(i);
		}

		// 8. while文
		int a8 = 1;
		while (a8 <= 10) {
			if (a8 % 2 == 0) {
				System.out.println("Hello" + a8);
			}
			a8++;
		}

		// 9. while文にbreakを使う
		int a9 = 1;
		while (a9 <= 10) {
			System.out.println("break前" + a9);
			a9++;
			break;
		}
		System.out.println("break後" + a9);

		// 10. 配列
		// int型しか扱わない配列型変数arrayを宣言して、3つのint型の集合で配列をつくる

		// 配列の宣言と初期化
		int[] array = { 10, 20, 30 }; // 省略系の初期化は変数の宣言と同時でないとならない

		// １つ１つ代入する書き方
		//		int[] array = new int[3];
		//		array[0] = 10;
		//		array[1] = 20;
		//		array[2] = 30;

		// array.lengthで配列の要素が数えられる
		// array.lengthで繰り返し回数を指定
		for (int i = 0; i < array.length; i++) {
			System.out.println("普通のfor文: " + array[i]);

		}

		// 11. 拡張for文

		// arrayの中身をnumに入れていく
		for (int num : array) {
			System.out.println("拡張for文: " + num);
		}

		// 12. メソッド　mainの中で実行する
		int a12 = 10; // helloメソッドの中と同じ変数名を宣言
		System.out.println("mainメソッドの中身のa12: " + a12);
		hello();

		// 13. メソッド　引数を受け取る
		int a13 = 111;
		System.out.println("hello2メソッドに引数" + a13 + "を渡す");
		hello2(a13);

		// 14. 引数
		int a = 10;
		int result = hello3(a, 20);
		System.out.println("hello3メソッドの実行結果は: " + result);

	}

	// 12. メソッド　helloメソッドの作成
	public static void hello() {
		int a12 = 20; // mainの中身と同じ変数名を宣言
		System.out.println("helloメソッドの実行結果は: " + a12);
	}

	// 13. メソッド　引数を受け取る
	public static void hello2(int num) {
		System.out.println("hello2メソッドの実行結果は: " + num);
	}

	// 14. メソッド int型のデータを戻す
	public static int hello3(int a14, int b14) {
		int result = a14 + b14;
		return result;
	}

}
