/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(s) {
    let n = s.length;
    let prev = -n;
    let ans = new Array(n).fill(0);

    for(let i = 0; i < n; i++){
        if(s[i] == 1){
            prev = i;
        }
        ans[i] = i - prev;
    }

    prev = 2 * n;
    for(let j = n-1; j >= 0; j--){
        if(s[j] == 1){
            prev = j;
        }
        ans[j] = Math.min((prev - j), ans[j]);
    }

    return Math.max(...ans);
};
