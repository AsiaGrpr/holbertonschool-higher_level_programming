#!/usr/bin/node

if (process.argv.length > 3) {
  const arg = process.argv.slice(2);
  arg.sort((a, b) => b - a);
  console.log((arg[1]));
} else {
  console.log(0);
}
