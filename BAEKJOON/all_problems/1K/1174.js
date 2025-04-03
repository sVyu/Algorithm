const fs = require('fs');
const n = Number(fs.readFileSync(0, 'utf-8').trim());
// console.log(n);

const arr = [];
let cnt = 0;

const btr = (max_len_arr, len_arr) => {
  if (max_len_arr == len_arr) {
    ++cnt;
    if (cnt == n) {
      console.log(arr.join(''));
      return true;
    }
  }

  for (let k = 0; k <= 9; ++k) {
    if (len_arr == 0 || (len_arr >= 1 && arr[len_arr - 1] > k)) {
      arr.push(k);
      if (btr(max_len_arr, len_arr + 1)) return true;
      arr.pop();
    }
  }
};

for (let max_len_arr = 1; max_len_arr <= 10; ++max_len_arr) {
  if (btr(max_len_arr, 0)) return;
}

console.log(-1);
