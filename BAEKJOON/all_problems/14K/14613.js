// S1 너의 티어는?
const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);
const [w, l, d] = inputData;
// console.log(w, l, d);

const dp = [];
for (let i = 0; i <= 20; ++i) {
  dp[i] = [];
  for (let j = 0; j <= 60; j++) {
    dp[i][j] = 0;
  }
}
// console.log(dp);

dp[0][40] = 1;
for (let i = 1; i <= 20; ++i) {
  for (let j = 0; j <= 60; ++j) {
    if (j + 1 <= 60) {
      dp[i][j] += dp[i - 1][j + 1] * l;
    }
    dp[i][j] += dp[i - 1][j] * d;
    if (j - 1 >= 0) {
      dp[i][j] += dp[i - 1][j - 1] * w;
    }
  }
}
// console.log(dp[20]);

for (const [l, r] of [
  [20, 30],
  [30, 40],
  [40, 50],
  [50, 60],
  [60, 61],
]) {
  // console.log(l, r);
  let sum = 0;
  for (let i = l; i < r; ++i) {
    sum += dp[20][i];
  }
  console.log(sum.toFixed(8));
}
