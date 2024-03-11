#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  if (typeof a === 'number' && typeof b === 'number' && Number.isInteger(a) && Number.isInteger(b)) {
    const sum = a + b;
    console.log(sum);
  } else {
    console.log('NaN');
  }
}

add(Number(argv[2]), Number(argv[3]));
