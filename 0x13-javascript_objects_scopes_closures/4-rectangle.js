#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j, s;
    for (i = 1; i <= this.height; i++) {
      s = '';
      for (j = 1; j <= this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    const dWidth = 2 * this.width;
    const dHeight = 2 * this.height;
    this.width = dWidth;
    this.height = dHeight;
  }
}

module.exports = Rectangle;
