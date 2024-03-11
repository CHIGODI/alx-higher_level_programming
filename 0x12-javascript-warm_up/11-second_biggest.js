#!/usr/bin/node

const { argv } = require('node:process');

if (!argv || argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  numbers.sort((a, b) => b - a);

  let large = numbers[0];
  let secondLargest = numbers[1];

  for (let i = 2; i < numbers.length; i++) {
    if (numbers[i] > large) {
      secondLargest = large;
      large = numbers[i];
    } else if (numbers[i] > secondLargest) {
      secondLargest = numbers[i];
    }
  }

  console.log(secondLargest);
}
