#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (isNaN(argv[2]) !== true) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
} else {
  console.log('Missing size');
}
