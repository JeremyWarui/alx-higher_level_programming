#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body.body);
    console.log(data.title);
  }
});
