#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Sqr extends Square {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
