#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) console.log(err);
  else {
    const obj = {};
    const tasks = JSON.parse(res.body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (obj[tasks[i].userId] === undefined) {
          obj[tasks[i].userId] = 0;
        } else {
          obj[tasks[i].userId]++;
        }
      }
    }
    console.log(obj);
  }
});
