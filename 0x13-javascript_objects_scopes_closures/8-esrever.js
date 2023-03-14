#!/usr/bin/node
exports.esrever = function (list) {
    const copy = [];
    let i = 0;
    while (i < list.length - 1) {
        i++;
    }
    // console.log(i);
    while (i >= 0) {
        copy.push(list[i]);
        i--;
    }

    return copy;
};
