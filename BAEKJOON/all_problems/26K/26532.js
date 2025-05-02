const fs = require('fs');
inputData = fs
  .readFileSync(0, 'utf-8')
  .toString()
  .trim()
  .split(' ')
  .map(Number);
const [n, m] = inputData;

console.log(Math.ceil((n * m) / (5 * 4840)));
