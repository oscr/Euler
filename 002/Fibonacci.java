public class Fibonacci {

	public static void main(String[] args) {
		int i = 1;
		int j = 2;
		int sum = 0;
		do {
			if (j % 2 == 0) {
				sum += j;
			}

			int k = i;
			i = j;
			j = i + k;

		} while (j < 4_000_000);

		System.out.println(sum);
	}

}