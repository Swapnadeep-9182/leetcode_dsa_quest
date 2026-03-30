import java.util.*;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // 1. Use Generics for type safety
        Map<Integer, Integer> nextGreaterMap = new HashMap<>();
        Stack<Integer> stack = new Stack<>();

        // Logic to map each number in nums2 to its next greater element
        for (int num : nums2) {
            while (!stack.isEmpty() && num > stack.peek()) {
                nextGreaterMap.put(stack.pop(), num);
            }
            stack.push(num);
        }

        // 2. Fill the result array using the map
        int[] result = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            // If the number wasn't in the map, it means there was no greater element
            result[i] = nextGreaterMap.getOrDefault(nums1[i], -1);
        }

        // 3. Return after the loop finishes, not inside it
        return result;
    }
}

