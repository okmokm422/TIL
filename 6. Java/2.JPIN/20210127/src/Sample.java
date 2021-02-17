public class Sample {
	public static void main(String[] args) {

		try {
			//			int[] array = new int[0];
			//			array[0] = 10;

			//			A a = null; // aの中身がない
			//			a.hello();

			int result = Integer.parseInt("a");
			System.out.println(result * 2);

			//		} catch (ArrayIndexOutOfBoundsException e) {
			//			System.out.println("touble array");
			//		} catch (NullPointerException e) {
			//			System.out.println("touble NullPo");
		} catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
			System.out.println("trouble array or nullpo");
			System.out.println("Message");
			System.out.println(e.getMessage());
		} catch (NumberFormatException e) {
			System.out.println("trouble number exception");
			System.out.println("Message");
			System.out.println(e.getMessage());
		}
		System.out.println("out of try ~ catch");

	}
}
