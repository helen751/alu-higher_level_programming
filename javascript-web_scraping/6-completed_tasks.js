#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  try {
    const todos = JSON.parse(body);
    const completedByUser = {};
    for (const t of todos) {
      if (t && t.completed === true) {
        const uid = String(t.userId);
        if (!completedByUser[uid]) {
          completedByUser[uid] = 0;
        }
        completedByUser[uid]++;
      }
    }
    console.log(completedByUser);
  } catch (e) {
    console.log(e);
  }
});
