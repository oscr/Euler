public class DivisibleTriangularNumber {
	public static void main(String[] args) {
		int triangle = 0;
		for (int i = 0; countDivisors(triangle) <= 500; triangle += i, i++)
			;
		System.out.println(triangle);
	}

	public static int countDivisors(int n) {
		int count = 0;
		for (int i = 1; i <= Math.sqrt(n); i++) {
			if (n % i == 0) {
				count += 2;
			}
		}
		return count;
	}
}
