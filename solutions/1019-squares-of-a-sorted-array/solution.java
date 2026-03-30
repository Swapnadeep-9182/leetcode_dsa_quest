import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        
        // Square each element
        for (int i = 0; i < nums.length; i++) {
            result[i] = nums[i] * nums[i];
        }
        
        // Sort the resulting array
        Arrays.sort(result);
        
        return result;
    }
}

