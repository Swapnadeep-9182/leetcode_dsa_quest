class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List duplicates = new ArrayList<>();
        Set seen = new HashSet<>();

        for(int num : nums){
            // if the number is already in the set, it's a duplicate
            if(seen.contains(num)){
                duplicates.add(num);
            }else{
                //Otherwise, add it to the set
                seen.add(num);
            }
        }
        return duplicates;
    }
}
