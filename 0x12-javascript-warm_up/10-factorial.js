#!/usr/bin/node
function fac (x) {
  if (x === 1 || isNaN(x)) {
    return (1);
  }
  return (x * fac(x - 1));
}

console.log(fac(parseInt(process.argv[2])));
