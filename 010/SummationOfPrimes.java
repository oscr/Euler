import java.util.Arrays;

public class SummationOfPrimes {

	public static void main(String[] args) {
		int limit = 2_000_000;
		boolean[] primes = new boolean[limit];

		// Initialize the array
		Arrays.fill(primes, Boolean.TRUE);
		primes[0] = false;
		primes[1] = false;

		// Calculate the prime sum
		long sum = 0;
		for (int i = 2; i < limit; i++) {
			if (primes[i]) {
				sum += i;
				for (long j = (long)i * i; j < primes.length; j += i) {
					primes[(int) j] = false;
				}
			}
		}
		System.out.println(sum);
	}
}