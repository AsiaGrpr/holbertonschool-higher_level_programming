#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (isNaN(argv[2]) !== true) {
  console.log('My number:', argv[2]);
} else {
  console.log('Not a number');
}
