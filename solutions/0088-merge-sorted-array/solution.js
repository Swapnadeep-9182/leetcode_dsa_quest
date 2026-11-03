/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (A, m, B, n) {
    let idx = m + n - 1;
    let i = m - 1;
    let j = n - 1;

    while (i >= 0 && j >= 0) {
        // Use post-decrement to assign and move the pointer in one line
        A[idx--] = (A[i] >= B[j]) ? A[i--] : B[j--];
    }

    // Only B needs a cleanup loop because if A has leftover elements, 
    // they are already in their correct, final positions.
    while (j >= 0) {
        A[idx--] = B[j--];
    }
};

