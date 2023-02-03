/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  var str1 = "a x a";
  var expected1 = true;
  
  var str2 = "racecar";
  var expected2 = true;
  
  var str3 = "Dud";
  var expected3 = false;
  
  var str4 = "oho!";
  var expected4 = false;
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
  function isPalindrome(str) {}
  
  /*****************************************************************************/
  









  
  /**
   * @param {string} str
   * @returns {boolean}
   */
  function isPalindrome(str = "") {
    for (var i = 0; i < Math.floor(str.length / 2); i++) {
      // Looping inwards from both sides.
      var leftChar = str[i];
      var rightChar = str[str.length - 1 - i];
  
      if (leftChar !== rightChar) {
        return false; // early exit
      }
    }
    return true;
  }
  
  /**
   * - Time: O(3n) -> O(n) linear. Each method used is looping.
   * - Space: O(2n) linear. Split and join both create a copy.
   * @param {string} str
   * @returns {boolean}
   */
  const functionIsPalindrome = (str = "") =>
    str === str.split("").reverse().join("");
  
  module.exports = { isPalindrome, functionIsPalindrome };
  