const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').split('\n');

const [n, k] = inputData[0].split(' ');
let zs = inputData[1].split(',').map(Number);
// console.log(n, k);
// console.log(zs);

for (let round = 0; round < k; ++round) {
  let new_zs = [];
  for (let i = 0; i < zs.length - 1; ++i) {
    new_zs.push(zs[i + 1] - zs[i]);
  }
  zs = new_zs;
}

// console.log(zs);
console.log(zs.join(','));
