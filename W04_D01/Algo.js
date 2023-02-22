function repeatHello(n) {
    var result = ""
    for(var i=0; i<n ; i++){
        result += "Hello \n"
    }
    return result
}

// console.log(repeatHello(3));


function repeatHelloRecursive(n){
    if(n==1){
        return "Recursive Hello\n"
    }
    return "Recursive Hello\n" + repeatHelloRecursive(n-1)
}
// console.log(repeatHelloRecursive(3));

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;


function x(n) {
    var int = parseInt(n)
    if(int<1){
        return 0
    }
    if(int == 1 ){
        return int
    }
    return int + x(int-1)
}
console.log(x(50.5));

// console.log(parseInt(50));