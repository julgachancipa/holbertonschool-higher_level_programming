#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);

const mList = [];
list.map((item, i) => {
  mList[i] = item * i;
});

console.log(mList);
