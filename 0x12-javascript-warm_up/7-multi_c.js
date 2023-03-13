#!/usr/bin/node
const num = process.argv[2];
if (+num) {
  let i;
  for (i = 1; i <= num; i++) {
    console.log('C is fun');
  }
} else if (!(+num)) {
  console.log('Missing number of occurrences');
}
