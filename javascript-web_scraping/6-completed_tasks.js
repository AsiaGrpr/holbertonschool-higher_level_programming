#!/usr/bin/node

const process = require('process');
const Request = require('request');

Request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  else {
    const count = {};
    JSON.parse(body).forEach(task => {
      if (task.completed) {
        const id = task.userId;
        if (!count[id]) { count[id] = 1; } else { count[id]++; }
      }
    });
    console.log(count);
  }
});
