#!/usr/bin/node

const { argv } = require('node:process');
const concatSentence = `${argv[2]} is ${argv[3]}`;

console.log(concatSentence);
