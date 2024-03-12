#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  while (list.length > 0) {
    const popped = list.pop();
    reversedList.push(popped);
  }
  return reversedList;
};
