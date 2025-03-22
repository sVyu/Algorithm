const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8');
// console.log(inputData);

const n = inputData.length;
let ans = inputData[0];
let pre = inputData[0];

for (let i = 1; i < n; ++i) {
  if (pre == inputData[i]) continue;
  pre = inputData[i];
  ans += inputData[i];
}

console.log(ans);
