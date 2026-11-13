/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let s = flowerbed.length;
    if(n==0){
        return true;
    }
    let cnt = 0;
    for(let i = 0; i < s; i++){
        if(flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (flowerbed[i+1] == 0 || i == s-1)){
            flowerbed[i] = 1;
            n--;
            if(n == 0){
                return true;
            }
        }
    }
    return false;
};
