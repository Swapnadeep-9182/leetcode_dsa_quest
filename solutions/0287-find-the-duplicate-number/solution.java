import java.util.HashMap;

class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int num : nums) {
            // Check if the number is already in the map
            if (map.containsKey(num)) {
                return num; // Return the duplicate immediately
            }
            // Otherwise, add it to the map
            map.put(num, 1);
        }
        
        return -1; // Default case if no duplicate is found
    }
}

