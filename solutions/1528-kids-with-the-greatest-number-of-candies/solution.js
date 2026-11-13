/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let n = candies.length;
    let res = new Array(n).fill(false);
    let bigCandy = Math.max(...candies);
    for(let i = 0; i < n; i++){
        if((candies[i] + extraCandies) >= bigCandy){
            res[i] = true;
        }
    }
    return res;
};
