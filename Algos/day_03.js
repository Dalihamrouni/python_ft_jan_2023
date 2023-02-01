/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

var arr1 = [1, 2, 3];
var separator1 = ", ";
var expected1 = "1, 2, 3";

var arr2 = [1, 2, 3];
var separator2 = "-";
var expected2 = "1-2-3";

var arr3 = [1, 2, 3];
var separator3 = " - ";
var expected3 = "1 - 2 - 3";

var arr4 = [1];
var separator4 = ", ";
var expected4 = "1";

var arr5 = [];
var separator5 = ", ";
var expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
  var expected = ""
  for(var i = 0; i<arr.length;i++) {
    if(i<arr.length -1 ){
      expected+= arr[i]+separator
    }else{
      expected+=arr[i]
    }
  }
  return expected
}

/*****************************************************************************/

console.log(join(arr1,separator1))