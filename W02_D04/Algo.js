/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

var str1 = "Y(3(p)p(3)r)s";
var expected1 = true;

var str2 = "N(0(p)3";
var expected2 = false;
// Explanation: not every parenthesis is closed.

var str3 = "N(0)t ) 0(k";
var expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

var str4 = "a(b))(c";
var expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.

 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    var arr = []
    for(var i =0;i<str.length; i++){
        if(str[i] == "(" || str[i] == ")"){
            arr.push(str[i])
        }
    }
    console.log(arr);
    if(arr[0] == ")"){
        return false
    }else {
        for(var j =0; j< arr.length/2; j++) {
        if(arr[j]!=arr[arr.length-j-1]) {
            continue
        }else {
            return false
        }
    }
    return true
    }
    
}
console.log(parensValid(str2))


