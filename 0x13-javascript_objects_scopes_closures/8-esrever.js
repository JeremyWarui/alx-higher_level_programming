#!/usr/bin/node
exports.esrever = function (list) {
  const copy = [];
  let i = 0;
  while (i < list.length - 1) {
    i++;
  }

  for (; i >= 0; i--) {
    copy.push(list[i]);
  }

  return copy;
};
