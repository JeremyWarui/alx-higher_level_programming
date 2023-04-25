#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) console.log(err);
  else {
    const obj = {};
    const body = JSON.parse(res);
    for (const i in body) {
      if (body[i].completed) {
        if (obj[body[i].userId] === undefined) {
          obj[body[i].userId] = 0;
        } else {
          obj[body[i].userId]++;
        }
      }
    }
    console.log(obj);
  }
});
