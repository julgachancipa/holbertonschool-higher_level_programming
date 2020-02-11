#!/usr/bin/node
const request = require('request');

const requestURL = process.argv[2];
request.get(requestURL, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const comUser = {};
    const todosList = JSON.parse(body);
    todosList.forEach(todo => {
      const usrId = todo.userId;
      if (!(usrId in comUser)) {
        comUser[usrId] = 0;
      }
      if (todo.completed === true) {
        comUser[usrId] += 1;
      }
    });
    console.log(comUser);
  }
});
