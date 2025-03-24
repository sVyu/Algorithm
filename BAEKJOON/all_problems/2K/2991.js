const fs = require('fs');
const inputData = fs
  .readFileSync(0, 'utf-8')
  .split('\n')
  .map((e) => e.split(' ').map(Number));

const [a, b, c, d] = inputData[0];
for (let k of inputData[1]) {
  let ans = 0;

  for (let [m, n] of [
    [a, b],
    [c, d],
  ]) {
    let res = k % (m + n);
    if (res > 0 && res <= m) ++ans;
  }

  console.log(ans);
}
