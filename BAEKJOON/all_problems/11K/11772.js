fs = require('fs');
const lines = fs.readFileSync(0, 'utf-8').trim().split('\n');
// console.log(input);

let ans = 0;
lines
  .slice(1)
  .map(
    (el) => (ans += Math.pow(parseInt(el.slice(0, -1)), parseInt(el.slice(-1))))
  );
console.log(ans);
