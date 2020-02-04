#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  const xStr = 'X'.repeat(process.argv[2]);
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(xStr);
  }
}
