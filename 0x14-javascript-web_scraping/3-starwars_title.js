#!/usr/bin/node
const request = require('request');

const requestURL = 'http://swapi.co/api/films/' + process.argv[2];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
