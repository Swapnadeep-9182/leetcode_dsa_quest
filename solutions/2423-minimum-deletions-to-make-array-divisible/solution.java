import java.util.Arrays;

class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        // 1. Find the GCD of all elements in numsDivide
        // Any number that divides all elements in numsDivide must divide their GCD.
        int targetGcd = numsDivide[0];
        for (int i = 1; i < numsDivide.length; i++) {
            targetGcd = gcd(targetGcd, numsDivide[i]);
            // Optimization: If GCD becomes 1, no smaller common divisor exists.
            if (targetGcd == 1) break;
        }

        // 2. Sort nums to easily find the smallest element that divides the GCD
        Arrays.sort(nums);

        // 3. Find the first (smallest) element in nums that divides the targetGcd
        for (int i = 0; i < nums.length; i++) {
            if (targetGcd % nums[i] == 0) {
                // The index 'i' represents the number of elements smaller than nums[i] 
                // that must be deleted.
                return i;
            }
            // Optimization: If current nums[i] is greater than the targetGcd, 
            // no subsequent element (being larger) can divide it.
            if (nums[i] > targetGcd) break;
        }

        return -1;
    }

    // Standard optimized Euclidean algorithm using modulo
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

