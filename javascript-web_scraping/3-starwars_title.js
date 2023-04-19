#!/usr/bin/node

const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (err, response, body) => {
  if (err) throw err;
  else {
    console.log(JSON.parse(body).title);
  }
});
