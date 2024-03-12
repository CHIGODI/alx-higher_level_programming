#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof (w) === 'number' && typeof (h) === 'number' && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let diagram;
    for (let i = 0; i < this.height; i++) {
      diagram = '';
      for (let j = 0; j < this.width; j++) {
        diagram += 'X';
      }
      console.log(diagram);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
