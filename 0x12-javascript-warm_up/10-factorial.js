#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (a) {
  if (!a || a === 1) {
    return 1;
  } else {
    return factorial(a - 1) * a;
  }
}

console.log(factorial(num));
