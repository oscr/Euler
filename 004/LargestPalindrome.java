public class LargestPalindrome {

	public static void main(String[] args) {
		int largest = -1;
		for (int i = 100; i < 1000; i++) {
			for (int j = 100; j < 1000; j++) {
				int l = j * i;
				if (l > largest && isPalindrome(l)) {
					largest = l;
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