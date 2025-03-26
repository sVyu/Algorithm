const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').split('\n');
// console.log(inputData);

n = Number(inputData[0]);
zs = inputData[1].split(' ').map(Number);
x = Number(inputData[2]);
// console.log(zs);

// z가 1인 경우 - 1이 1개, 1이 2개 이상, 1이 3개 이상
// 1이 나타날 수 있는 모든 경우 처리
num_one_idxs = [];
for (let i = 0; i <= n; ++i) {
  if (zs[i] == 1) {
    num_one_idxs.push(i);
  }
}
// console.log(num_one_idxs);

if (num_one_idxs.length >= 3) {
  console.log('NO');
  return;
} else if (num_one_idxs.length == 2) {
  const [i1, i2] = num_one_idxs;
  if (i2 - i1 == x) {
    console.log('YES');
    console.log(i1, i2);
  } else {
    console.log('NO');
  }
  return;
} else if (num_one_idxs.length == 1) {
  const i = num_one_idxs[0];
  if (i + x <= n && zs[i + x] >= 1) {
    console.log('YES');
    console.log(i, i + x);
  } else if (i - x >= 0 && zs[i - x] >= 3) {
    console.log('YES');
    console.log(i - x, i);
  } else {
    console.log('NO');
  }
  return;
}

// z가 3이상인 경우
num_three_idxs = [];
for (let i = 0; i <= n; ++i) {
  if (zs[i] >= 3) {
    num_three_idxs.push(i);
  }
}

for (let i of num_three_idxs) {
  if (i + x <= n && zs[i + x] >= 1) {
    console.log('YES');
    console.log(i, i + x);
    return;
  }
}
console.log('NO');
