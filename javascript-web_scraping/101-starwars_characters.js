#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  try {
    const data = JSON.parse(body);
    const chars = data.characters || [];

    const printInOrder = (idx) => {
      if (idx >= chars.length) return;
      request(chars[idx], (cerr, _cres, cbody) => {
        if (cerr) {
          console.log(cerr);
          return;
        }
        try {
          const cdata = JSON.parse(cbody);
          console.log(cdata.name);
          printInOrder(idx + 1);
        } catch (e) {
          console.log(e);
        }
      });
    };
    printInOrder(0);
  } catch (e) {
    console.log(e);
  }
});
