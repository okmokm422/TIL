// 仕様変更に対応するための新しいクラス
// 既存のコード変更なしに変更可能
// あとはFactoryクラスをreturn C();にするだけ
public class C extends A {
	@Override
	public void hello() {
		System.out.println("C");
	}

}
