#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const requestURL = process.argv[2];
const fileName = process.argv[3];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
