const fs = require('fs');
const input_data = fs.readFileSync(0, 'utf-8').trim().split('\n');
// console.log(input_data);

const k = Number(input_data[0]);
const n = Number(input_data[1]);

let ts = input_data[2];
const ladders = input_data.slice(3);
// console.log(ladders);

const question_mark_idx = ladders.findIndex((el, idx) => el[0] == '?');
// console.log(question_mark_idx);

const move_by_ladder = (k, s, ladder) => {
  s = s.split('');
  for (let i = 0; i < k - 1; ++i) {
    if (ladder[i] == '-') {
      const tmp = s[i];
      s[i] = s[i + 1];
      s[i + 1] = tmp;
    }
  }
  s = s.join('');
  return s;
};

let bs = '';
for (let i = 0; i < k; ++i) {
  bs += String.fromCharCode(65 + i);
}
// console.log(bs);

for (let i = 0; i < question_mark_idx; ++i) {
  bs = move_by_ladder(k, bs, ladders[i]);
}
// console.log(bs);

for (let i = n - 1; i > question_mark_idx; --i) {
  ts = move_by_ladder(k, ts, ladders[i]);
}
// console.log(ts);

let ans = '';
let i = 0;
let pos = true;

while (i < k - 1) {
  if (bs[i] == ts[i]) {
    ans += '*';
    ++i;
  } else if (bs[i] == ts[i + 1] && bs[i + 1] == ts[i]) {
    ans += '-';
    if (i + 1 < k - 1) ans += '*';
    i += 2;
  } else {
    pos = false;
    break;
  }
}

if (!pos) {
  console.log(
    Array.from({ length: k - 1 })
      .map((el) => 'x')
      .join('')
  );
  return;
}
console.log(ans);
