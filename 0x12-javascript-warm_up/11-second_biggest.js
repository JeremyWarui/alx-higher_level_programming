#!/usr/bin/node
const arrayNums = process.argv.slice(2);
function sndMax (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((x, y) => x - y);
    arr.pop();
    return (arr.pop());
  }
}
console.log(sndMax(arrayNums));
