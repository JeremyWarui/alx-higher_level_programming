#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body.body);
    const chars = data.characters;
    for (const i in chars) {
      request(chars[i], (err, body) => {
        if (!err) {
          const name = JSON.parse(body.body).name;
          console.log(name);
        }
      });
    }
  }
});
