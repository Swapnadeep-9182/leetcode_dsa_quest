/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let num = BigInt(digits.join(""));
    num += 1n;
    return String(num).split("").map(Number);
};
