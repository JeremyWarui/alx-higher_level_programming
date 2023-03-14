#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i, j, s;
    for (i = 1; i <= this.height; i++) {
      s = '';
      for (j = 1; j <= this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
