class Solution {
    public int jump(int[] nums) {
        int jumps=0, currentEnd = 0, maxReach = 0;
        int n = nums.length;
        for(int i=0; i<(n-1); i++){
            maxReach = Math.max(maxReach, i+nums[i]);
            if(i == currentEnd){
                jumps++;
                currentEnd = maxReach;
            }
        }
        return jumps;
    }
}
