
// 抽象クラス
// 固定の部分はTemplateクラスで引き受けている
// ベテランが担当するイメージの場所

public abstract class Template {

	// Templateクラスではexecuteメソッドしか外部から呼び出せない
	public void execute() {
		System.out.println("start");
		this.perform();
		System.out.println("end");
	}

	// protectedは他のパッケージから呼び出せない
	protected abstract void perform();
}
