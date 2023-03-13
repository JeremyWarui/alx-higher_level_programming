#!/usr/bin/node
exports.callMeMoby = function (x, callFunc) {
  let i;
  for (i = 0; i < x; i++) {
    callFunc();
  }
};
