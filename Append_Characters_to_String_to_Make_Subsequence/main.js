/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    num = 0;
    j = 0;
    for(let i = 0; i < s.length; i++){
        if(s[i] === t[j]){
            j += 1;
            num += 1;
        }
    }
    return t.length - num;
};
