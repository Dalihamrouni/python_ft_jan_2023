/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

var arr1 = ["a", "a", "a"];
var expected1 = {
  a: 3,
};

var arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
var expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {}





function makeFrequencyTable(arr = []) {
  var freqTable = {};

  for (var i = 0;i<arr.length; i++) {
    if (freqTable.hasOwnProperty([arr[i]]) == false) {
      // first occurrence found
      freqTable[arr[i]] = 1;
    }
    else {
        freqTable[arr[i]]++;
    }
  }

  return freqTable;
}
console.log(makeFrequencyTable(arr1))
console.log(makeFrequencyTable(arr2))