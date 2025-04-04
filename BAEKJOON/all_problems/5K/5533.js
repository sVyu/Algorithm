const fs = require('fs');
const input_data = fs.readFileSync(0, 'utf-8').trim().split('\n');
// console.log(input_data);

const n = Number(input_data[0]);
const numbers_by_players = input_data
  .slice(1)
  .map((el) => el.split(' ').map(Number));
// console.log(scores);

const idx_arr = Array.from({ length: n }).map((_, i) => i);
const ans_scores = Array.from({ length: n }).fill(0);
// const ans_scores = Array.from({ length: n }).map(() => 0);
// console.log(ans_scores);

const scores_by_rounds = [0, 1, 2].map((column) => {
  const num_set = {};
  // round별 등장한 숫자들 set에 저장
  idx_arr.map((row) => {
    if (numbers_by_players[row][column] in num_set) {
      num_set[numbers_by_players[row][column]] += 1;
    } else {
      num_set[numbers_by_players[row][column]] = 1;
    }
  });
  //   console.log(num_set);

  idx_arr.map((row) => {
    if (num_set[numbers_by_players[row][column]] == 1) {
      ans_scores[row] += numbers_by_players[row][column];
    }
  });
});

ans_scores.map((el) => console.log(el));
