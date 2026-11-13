/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = new Set(["a","e","i","o","u"]);
    const chars = s.split("");
    let leftPointer = 0;
    let rightPointer = chars.length - 1;
    while (leftPointer < rightPointer){
        if(!vowels.has(chars[leftPointer].toLowerCase())){
            leftPointer++;
        }else if(!vowels.has(chars[rightPointer].toLowerCase())){
            rightPointer--;
        }else{
            [chars[leftPointer],chars[rightPointer]] = [chars[rightPointer],chars[leftPointer]];
            leftPointer++;
            rightPointer--;
        }
    }
    return chars.join("");
};
