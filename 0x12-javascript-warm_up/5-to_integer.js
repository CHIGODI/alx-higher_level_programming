#!/usr/bin/node

const { argv } = require('node:process');
const firstArg = parseInt(argv[2]);

if (isNaN(firstArg) || !firstArg) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
