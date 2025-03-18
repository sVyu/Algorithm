const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);
console.log(inputData);
// const inputData = fs.readFileSync("./input.txt").toString().split(' ').map(Number);

const base = 2024*12;
const date = base + parseInt(inputData)*7;

console.log(parseInt(date/12),  (date%12)+1);