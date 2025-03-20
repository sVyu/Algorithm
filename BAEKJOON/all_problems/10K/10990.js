const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);
const n = inputData[0];

console.log(' '.repeat(n - 1) + '*');
for (let i = 1; i < n; ++i) {
  console.log(' '.repeat(n - i - 1) + '*' + ' '.repeat(2 * i - 1) + '*');
}
