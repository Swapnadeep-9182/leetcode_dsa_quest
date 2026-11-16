/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    let n = nums.length;

    let num1 = Number.POSITIVE_INFINITY;
    let num2 = Number.POSITIVE_INFINITY;

    for(let i = 0; i < n; i++){
        let num3 = nums[i];

        if(num3 <= num1){
            num1 = num3;
        }else if(num3 <= num2){
            num2 = num3;
        }else{
            return true;
        }
    }
    return false;
};
