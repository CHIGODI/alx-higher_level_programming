#!/usr/bin/node

const { argv } = require('node:process');
let count = 0;

for (let i = 2; i < argv.length; i++) {
  count++;
}

if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log('Argument found');
} else if (count > 1) {
  console.log('Arguments found');
}
