/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var digitSum = function(s, k) {
    while (s.length > k) {
        let next = "";
        const n = s.length;
        
        for (let i = 0; i < n; i += k) {
            let sum = 0;
            const end = i + k < n ? i + k : n;
            
            for (let j = i; j < end; j++) {
                sum += s.charCodeAt(j) - 48;
            }
            next += sum;
        }
        s = next;
    }
    return s;
};

