#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function factorialize (num) {
  if (num < 0) { return -1; } else if (num === 0) { return 1; } else {
    return (num * factorialize(num - 1));
  }
}

if (isNaN(argv[2]) !== true) {
  console.log(factorialize(Number(argv[2])));
} else {
  console.log(1);
}
