/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let n = chars.length;
    let idx = 0;

    for(let i = 0; i < n; i++){
        ch = chars[i];
        count = 0;
        while((i<n) && (chars[i] === ch)){
            count++;
            i++;
        }
        if(count == 1){
            chars[idx] = ch;
            idx++;
        }else{
            chars[idx] = ch;
            idx++;
            let str = count.toString();
            for(let j = 0; j<str.length;j++){
                chars[idx] = str[j];
                idx++;
            }
        }
        i--;
    }
    return idx;
};
