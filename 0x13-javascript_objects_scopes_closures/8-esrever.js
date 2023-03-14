#!/usr/bin/node
exports.esrever = function (list) {
  let beg = 0;
  let end = list.length - 1;
  let tmp;

  while (end > beg) {
    tmp = list[beg];
    list[beg] = list[end];
    list[end] = tmp;
    beg++;
    end--;
  }

  return list;
};
