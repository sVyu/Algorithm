const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);

const n = inputData[0];

const visited = [];
for (let i = 0; i <= n * 9; ++i) {
  visited[i] = false;
}

const recursion = (ni, result) => {
  if (n == ni) {
    visited[result] = true;
    return;
  }
  for (let k = 1; k <= 9; ++k) {
    recursion(ni + 1, result * k);
  }
};

recursion(0, 1);
console.log(
  visited.reduce((acc, curr) => {
    if (curr) return acc + 1;
    return acc;
  }, 0)
);
