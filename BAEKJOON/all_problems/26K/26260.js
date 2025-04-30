const fs = require('fs');
inputData = fs.readFileSync(0, 'utf-8').trim().split('\n');

n = Number(inputData[0]);
new_num = Number(inputData[2]);
zs = inputData[1]
  .split(' ')
  .map(Number)
  .map((el) => {
    if (el == -1) {
      el = new_num;
    }
    return el;
  })
  .sort((a, b) => a - b);

const ans = [];

// rec : recursion
const rec = (l, r) => {
  const mid = (l + r) / 2;
  if (mid == l) {
    ans.push(zs[mid]);
    return;
  }

  rec(l, mid - 1);
  rec(mid + 1, r);
  ans.push(zs[mid]);
};

rec(0, n - 1);
console.log(ans.join(' '));
