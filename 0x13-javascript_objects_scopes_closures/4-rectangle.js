#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const symbol = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(symbol);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.length;
    this.length = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
