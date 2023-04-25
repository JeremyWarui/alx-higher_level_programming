#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const idChar = 18;
let count = 0;

request(url, (err, body) => {
  if (err) console.log(err);
  else {
    const movies = JSON.parse(body.body).results;
    for (const i in movies) {
      const chars = movies[i].characters;
      for (const y in chars) {
        if (chars[y].includes(idChar)) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
