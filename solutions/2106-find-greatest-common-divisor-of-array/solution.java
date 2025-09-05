import java.util.*;
class Solution {
    public int findGCD(int[] nums) {
      Arrays.sort(nums);

      int smallest = nums[0];

      int largest = nums[nums.length-1];

      return gcd(largest,smallest);  
    }

    public int gcd(int a, int b){
        if(b==0){
            return a;
        }
        else{
            return gcd(b, a % b);
        }
    }
}
