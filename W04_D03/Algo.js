/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */

/*****************************************************************************/

function binarySearch(sortedNums, searchNum) {
    var leftIndex = 0;
    var rightIndex = sortedNums.length-1;
    while(leftIndex <= rightIndex){
        var mid = Math.floor(rightIndex-leftIndex /2)
        if (sortedNums[mid] == searchNum){
            return true
        }
        if (searchNum<sortedNums[mid]){
            rightIndex = mid -1 
        }else {
            leftIndex = mid +1
        }
    }
    return false
}

console.log(binarySearch(nums1, 3))