#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  else {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) throw err;
    });
  }
});
