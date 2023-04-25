#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, data) => {
  if (err) console.log(err);
  else {
    const body = JSON.parse(data);
    console.log(body.title);
  }
});
