class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
       int n = arr.length;
       int min_val = Arrays.stream(arr).min().getAsInt();
       int max_val = Arrays.stream(arr).max().getAsInt();
       if(max_val == min_val){
        return true;
       }
       int total_gap = max_val - min_val;
       if(total_gap % (n-1) != 0){
        return false;
       }
       int diff = total_gap/(n-1);
       HashSet<Integer> seen = new HashSet<>();
       for (int number : arr) {
            seen.add(number);
        }
        int current_step = min_val;
        for(int i = 0; i<=n-1; i++){
            if(!seen.contains(current_step)){
                return false;
            }
            current_step += diff;
        }
        return true;
    }
}
