#!/usr/bin/node

const { dict } = require('./101-data');

let newDict = {};
for (const key in dict) {
    if (dict.hasOwnProperty(key)) {
        let value = dict[key];
        if (!newDict[value]) {
            newDict[value] = [];
        }
        newDict[value].push(key);
    }
}

console.log(newDict);
