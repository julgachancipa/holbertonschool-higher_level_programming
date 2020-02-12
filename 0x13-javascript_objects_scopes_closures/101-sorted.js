#!/usr/bin/node
const dict = require('./101-data').dict;

const nDict = {};
for (const k in dict) {
  if (!(dict[k] in nDict)) {
    nDict[dict[k]] = [];
  }
  nDict[dict[k]].push(k);
}

console.log(nDict);
