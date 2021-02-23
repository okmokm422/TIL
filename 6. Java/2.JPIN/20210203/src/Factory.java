
public class Factory {

	public static A create() {
		return new C(); // ポリモーフィズムを使う 仕様変更でB→Cに変更

	}
}
