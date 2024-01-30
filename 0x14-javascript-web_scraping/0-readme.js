#!/usr/bin/node
// Reads and prints the content of a file

const argv = process.argv;
let fls = require('fs');
fls.readFile(argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
