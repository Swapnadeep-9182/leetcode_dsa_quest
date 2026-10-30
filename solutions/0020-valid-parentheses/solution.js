/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(str) {
    let st = [];

    for(let i = 0; i<str.length; i++){
        if(str[i] == "(" || str[i] == "{" || str[i] == "["){ //Opening brackets
            st.push(str[i]);
        }else{ // Closing Brackets
            if(st.length == 0){ // If Closing brackets are more in number
                return false
            }
            
            let topElement = st[st.length - 1];

            if((topElement == "(" && str[i] == ")") || (topElement == "{" && str[i] == "}") || (topElement == "[" && str[i] == "]")){
                st.pop();
            }else{ // no match found
                return false;
            }
        }
    }

    if(st.length == 0){ // If Opening Brackets are more in number
        return true;
    }else{
        return false;
    }
};
