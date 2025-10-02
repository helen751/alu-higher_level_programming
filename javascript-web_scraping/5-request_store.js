#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, { encoding: 'utf8' }, (werr) => {
    if (werr) {
      console.log(werr);
    }
  });
});
