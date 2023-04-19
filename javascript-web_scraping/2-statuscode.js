#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) throw err;
  else {
    console.log(`code: ${response.statusCode}`);
  }
});
