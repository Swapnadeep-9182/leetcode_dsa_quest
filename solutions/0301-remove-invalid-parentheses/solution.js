/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    const isValid = (str) => {
        let balance = 0;
        for (let char of str) {
            if (char === '(') balance++;
            else if (char === ')') balance--;
            if (balance < 0) return false;
        }
        return balance === 0;
    };
    let queue = new Set([s]);
    let result = [];
    let found = false;
    while (queue.size > 0) {
        const nextQueue = new Set();
        for (let curr of queue) {
            if (isValid(curr)) {
                result.push(curr);
                found = true;
            }
        }
        if (found) {
            return result;
        }
        for (let curr of queue) {
            for (let i = 0; i < curr.length; i++) {
                if (curr[i] !== '(' && curr[i] !== ')') continue; 
                const nextStr = curr.slice(0, i) + curr.slice(i + 1);
                nextQueue.add(nextStr);
            }
        }
        queue = nextQueue;
    }
    return [''];
};
