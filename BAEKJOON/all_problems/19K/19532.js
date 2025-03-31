const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);

const [a, b, c, d, e, f] = inputData;
// console.log(a, b, c, d, e, f);

for (let x = -999; x <= 999; ++x) {
  for (let y = -999; y <= 999; ++y) {
    if ((a * x + b * y == c) & (d * x + e * y == f)) {
      console.log(x, y);
      return;
    }
  }
}
