#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i, j, s;
      for (i = 1; i <= this.height; i++) {
        s = '';
        for (j = 1; j <= this.width; j++) {
          s += 'C';
        }
        console.log(s);
      }
    }
  }
}

module.exports = Square;
