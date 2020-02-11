#!/usr/bin/node
exports.esrever = function (list) {
  const rList = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    rList.push(list[i]);
  }
  return rList;
};
