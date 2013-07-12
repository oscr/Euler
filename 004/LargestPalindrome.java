public class LargestPalindrome {
	public static void main(String[] args) {
		int largest = Integer.MIN_VALUE;
		for (int i = 100; i < 1000; i++) {
			for (int j = 100; j < 1000; j++) {
				int k = j * i;
				if (k > largest && isPalindrome(k)) {
					largest = k;
				}
			}
		}
		System.out.println(largest);
	}

	public static boolean isPalindrome(int i) {
		String s1 = Integer.toString(i);
		String s2 = new StringBuilder(s1).reverse().toString();
		return s1.equals(s2);

	}
}
