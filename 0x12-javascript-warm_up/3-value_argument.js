#!/usr/bin/node
if (!process.argv[2]) {
  console.log('No argument');
} else {
  const args = process.argv.slice(2);
  for (const i in args) {
    console.log(args[i]);
  }
}
