/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */

function sumArr(nums,i=0) {
    if(i == nums.length){
        return 0
    }
    // console.log("i == ",i);
    return nums[i] + sumArr(nums, i+1)
}
console.log(sumArr(nums3));
/*****************************************************************************/

