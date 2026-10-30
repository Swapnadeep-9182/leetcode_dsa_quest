/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){
        return false;
    }
    
    if(x < 10){
        return true;
    }

    let rev = 0;
    let digitsLeft = x;

    while(digitsLeft > 0){
        let lastDigit = digitsLeft % 10;
        rev = (rev * 10) + lastDigit;
        digitsLeft = Math.floor(digitsLeft / 10);
    }

    if(rev == x){
        return true;
    }else{
        return false;
    }
};
