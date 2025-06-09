const fs = require('fs');
const zs = fs.readFileSync(0, 'utf-8').trim().split('\n');
// console.log(zs);

const results = zs.reduce((acc, z) => {
  if (z === '0') return acc;

  let ans = z.length + 1;
  for (c of z) {
    if (c === '1') ans += 2;
    else if (c === '0') ans += 4;
    else ans += 3;
  }
  return [...acc, ans];
}, []);

console.log(results.join('\n'));
