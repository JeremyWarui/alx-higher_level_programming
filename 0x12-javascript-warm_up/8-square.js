#!/usr/bin/node
const num = Number(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  let i, j, s;
  for (i = 1; i <= num; i++) {
    s = '';
    for (j = 1; j <= num; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
