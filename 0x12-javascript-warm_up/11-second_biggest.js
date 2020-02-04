#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let allArg = process.argv.slice(2);
  allArg.sort();
  allArg = allArg.map(Number);
  while (isNaN(allArg[allArg.length - 1])) {
    allArg.pop();
  }
  console.log(allArg);
  console.log(allArg[allArg.length - 2]);
}
