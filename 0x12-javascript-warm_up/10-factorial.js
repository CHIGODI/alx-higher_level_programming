#!/usr/bin/node

const { argv } = require('node:process');
const number = Number(argv[2]);
let factorial = 1;

if (number && !isNaN(number)) {
  for (let i = 1; i <= number; i++) {
    factorial *= i;
  }
  console.log(factorial);
} else {
  console.log(1);
}
