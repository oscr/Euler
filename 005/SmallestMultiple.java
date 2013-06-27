import java.math.BigInteger;

public class SmallestMultiple {

	public static void main(String[] args) {
		BigInteger sum = BigInteger.ONE;
		for (int i = 1; i <= 20; i++) {
			BigInteger bi = BigInteger.valueOf(i);
			sum = bi.divide(bi.gcd(sum)).multiply(sum);
		}

		System.out.println(sum);
	}

}
