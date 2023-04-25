#!/usr/bin/node
/* script that reads and prints the content of a file */
const fs = require('fs');

const file = process.argv[2];

fs.readFile(file, { encoding: 'utf8' }, function (err, data) {
  if (err) console.log(err);
  else {
    console.log(data);
  }
});
