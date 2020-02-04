#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const allArg = process.argv.slice(2);
  allArg.sort();
  console.log(allArg.length - 2);
}
