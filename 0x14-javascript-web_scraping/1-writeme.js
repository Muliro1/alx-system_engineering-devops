#!/usr/bin/node
// Writes a string to a file

const fls = require('fs');
const argv = process.argv;
let file_Path = argv[2];
let string = argv[3];

fls.writeFile(file_Path, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
