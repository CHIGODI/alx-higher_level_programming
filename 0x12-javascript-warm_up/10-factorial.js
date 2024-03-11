#!/usr/bin/node

const { argv } = require('node:process');
const number = Number(argv[2]);

function calculateFactorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * calculateFactorial(num - 1);
}

if (!isNaN(number)) {
  const result = calculateFactorial(number);
  console.log(result);
} else {
  console.log(1);
}
