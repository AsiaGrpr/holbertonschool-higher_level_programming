#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    const List = JSON.parse(body).results;

    let count = 0;
    for (const movies of List) {
      for (const character of movies.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
