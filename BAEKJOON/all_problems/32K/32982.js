const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split('\n');

const [n, k] = inputData[0].split(' ').map(Number);
const zs = inputData[1].split(' ').map(Number);

const se_times = [];
for (let i = 0; i < 3; ++i) {
  se_times.push([zs[2 * i], zs[2 * i + 1]]);
}
// console.log(se_times);

// medicine_work_time : mwt
let mwt = se_times[0][1];
for (let day = 1; day <= n; ++day) {
  for (let i = 0; i < 3; ++i) {
    if (day == 1 && i == 0) continue;

    mwt += k;
    if (mwt < se_times[i][0] + (day - 1) * 1440) {
      console.log('NO');
      return;
    }
    mwt = Math.min(mwt, se_times[i][1] + (day - 1) * 1440);
    // console.log(base);
  }
}
console.log('YES');
