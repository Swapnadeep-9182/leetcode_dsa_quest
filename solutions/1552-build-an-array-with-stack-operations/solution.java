class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> ans = new ArrayList<>();
        int target_index = 0;
        int current_number = 1;
        int length = target.length;
        while(current_number <= n){
            if(target_index == length){
                break;
            }
            if(current_number == target[target_index]){
                ans.add("Push");
                target_index++;
            }else{
                ans.add("Push");
                ans.add("Pop");
            }
            current_number++;
        }
        return ans;
    }
}
