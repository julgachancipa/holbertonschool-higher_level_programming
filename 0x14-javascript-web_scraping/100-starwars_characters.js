#!/usr/bin/node
const request = require('request');

const requestURL = 'http://swapi.co/api/films/' + process.argv[2];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const characList = JSON.parse(body).characters;
    characList.forEach(chURL => {
      request.get(chURL, function (chErr, chRes, chBody) {
        if (chErr) {
          console.log(chErr);
        } else {
          console.log(JSON.parse(chBody).name);
        }
      });
    }
    );
  }
});
