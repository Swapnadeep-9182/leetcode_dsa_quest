/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length;
    let ans = new Array(n).fill(1);

    for(let i = 1; i < n; i++){
        ans[i] = nums[i-1] * ans[i-1];
    }
//[1,1,2,6]
    let suffix = 1;
    for(let i = n-2; i>=0; i--){
        suffix = suffix * nums[i+1];//[24,12,4,1]
        ans[i] = suffix * ans[i]; 
    }
    return ans;
};
