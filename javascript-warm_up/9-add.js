#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function add (a, b) {
  return a + b;
}

if (isNaN(argv[2]) !== true || isNaN(argv[3] !== true)) {
  console.log(add(Number(argv[2]), Number(argv[3])));
} else {
  console.log(NaN);
}
