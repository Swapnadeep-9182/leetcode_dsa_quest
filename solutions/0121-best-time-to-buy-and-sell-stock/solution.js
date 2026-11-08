/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(arr) {
    let n = arr.length;
    let maxprofit = 0;
    let bestBuy = arr[0];

    for(let i = 1; i < n; i++){
        maxprofit = Math.max(maxprofit, (arr[i] - bestBuy));
        bestBuy = Math.min(bestBuy, arr[i]);
    }
    return maxprofit;
};
