#!/usr/bin/node
const request = require('request');

const requestURL = process.argv[2];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const filmsList = JSON.parse(body).results;
    filmsList.forEach(film => {
      const characters = film.characters;
      characters.forEach(ch => {
        if (ch.includes('/18/')) {
          counter += 1;
        }
      }
      );
    }
    );
    console.log(counter);
  }
});
