/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    //validation
    if(!Number.isInteger(n) || n <= 0){
        throw new Error("Input number must be a positive integer");
    }

    var ans = [];

    for(let i = 1; i<= n; i++){
        if(i%15==0){
            ans.push("FizzBuzz");
        }else if(i%3==0){
            ans.push("Fizz");
        }else if(i%5==0){
            ans.push("Buzz");
        }else{
            ans.push(i.toString());
        }
    }

    return ans;
};
