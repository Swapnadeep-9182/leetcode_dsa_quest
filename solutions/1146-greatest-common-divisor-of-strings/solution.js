/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    let i = str1.length;
    let j = str2.length;
    if(str1+str2!=str2+str1){
        return "";
    }

    return str1.slice(0,gcd(i,j));
};

function gcd(a,b){
    while(b!=0){
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
