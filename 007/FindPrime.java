public class FindPrime {

	public static void main(String[] args) {
		int primesLeftToFind = 10_000;
		int maybePrime = 1;
		do {
			maybePrime += 2;
			if (isPrime(maybePrime)) {
				primesLeftToFind--;
			}
		} while (primesLeftToFind > 0);
		System.out.println(maybePrime);
	}

	public static boolean isPrime(int n) {
		for (int i = 2; i < (int) Math.pow(n, 0.5) + 1; i++) {
			if (n % i == 0) {
				return false;

			}
		}
		return true;
	}
}