class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};

        // Find the first occurrence from the front
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                result[0] = i;
                break;
            }
        }

        // If the first occurrence isn't found, the target isn't in the array
        if (result[0] == -1) {
            return result;
        }

        // Find the first occurrence from the back
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] == target) {
                result[1] = i;
                break;
            }
        }

        return result;
    }
}

