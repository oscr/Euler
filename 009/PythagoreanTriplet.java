public class PythagoreanTriplet {

	public static void main(String[] args) {
		for (int a = 1; a < 1000; a++) {
			for (int b = 1; b < 1000; b++) {
				int c = 1000 - a - b;
				if (isPythagoreanTriplet(a, b, c)) {
					System.out.println(a * b * c);
					return;
				}
			}
		}
	}

	public static boolean isPythagoreanTriplet(int a, int b, int c) {
		return a * a + b * b == c * c;
	}

}