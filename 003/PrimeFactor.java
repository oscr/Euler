public class PrimeFactor {

	public static void main(String[] args) {
		long i = 600851475143L;
		long factor;
		for (factor = 2; factor < i; factor++) {
			if (i % factor == 0) {
				i /= factor;
				continue;
			}
		}

		System.out.println(factor);
	}

}
