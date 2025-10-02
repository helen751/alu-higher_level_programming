#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const WEDGE_ID = '18';
request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  try {
    const data = JSON.parse(body);
    const films = data.results || [];
    const count = films.reduce((acc, film) => {
      const characters = film.characters || [];
      const hasWedge = characters.some((c) => c.includes(`/people/${WEDGE_ID}/`));
      return acc + (hasWedge ? 1 : 0);
    }, 0);
    console.log(count);
  } catch (e) {
    console.log(e);
  }
});
