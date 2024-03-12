#!/usr/bin/node
/**
 * Defines a class Square that inherits from Rectangle
 */

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let diagram;
      for (let i = 0; i < this.height; i++) {
        diagram = '';
        for (let j = 0; j < this.width; j++) {
          diagram += c;
        }
        console.log(diagram);
      }
    }
  }
}
module.exports = Square;
