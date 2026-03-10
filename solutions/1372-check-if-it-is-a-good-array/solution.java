class Solution {
    public boolean isGoodArray(int[] nums) {
        // Reduced to one line for efficiency
        return findGCDOfArray(nums) == 1;
    }

    public static int findGCDOfArray(int[] arr) {
        if (arr == null || arr.length == 0) return 0;

        int result = arr[0];
        for (int i = 1; i < arr.length; i++) {
            // Replaced non-existent Math.gcd with custom method
            result = gcd(result, arr[i]);
            if (result == 1) return 1;
        }
        return result;
    }

    // Euclidean Algorithm to find GCD
    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

