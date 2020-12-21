package ex24;

public class InvokeMethod {

	public static void main(String[] args) {
		int price = calcTax(100);
		System.out.println(price);
	}

	public static int calcTax(int price) {
		int priceIncludeTax = (int) (price * 1.08);
		return priceIncludeTax;
	}

}
