/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function(s, c) {
    let n = s.length;
    let ans = new Array(n).fill(0);
    let prev = -n;

    for(let i = 0; i < n; i++){
        if(s[i] == c){
            prev = i;
        }
        ans[i] = i - prev;
    }

    prev = 2 * n;

    for(let i = n - 1; i >= 0; i--){
        if(s[i] == c){
            prev = i;
        }
        ans[i] = Math.min((prev - i), ans[i]);
    }

    return ans;
};
