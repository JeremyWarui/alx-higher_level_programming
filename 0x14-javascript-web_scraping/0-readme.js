#!/usr/bin/node
/* script that reads and prints the content of a file */
const { argv } = require('node:process');
const fs = require('fs');

const file = argv[1];
try {
  fs.readFileSync(file);
} catch (error) {
  throw (console.error(error));
}
