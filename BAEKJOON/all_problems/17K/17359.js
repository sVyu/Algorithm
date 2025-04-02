const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split('\n');
// console.log(inputData);

const n = inputData[0];
const arr = inputData.slice(1);
// console.log(n, arr);

// getPermutations ref : search
// https://velog.io/@jhsung23/JS-%EC%88%9C%EC%97%B4Permutation-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
const getPermutations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]); // 1���� ���� ��, �ٷ� ��� �迭�� ���� return

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)]; // �ش��ϴ� fixed�� ������ ������ �迭
    const permutations = getPermutations(rest, selectNumber - 1); // �������� ���� ������ ���Ѵ�.
    const attached = permutations.map((permutation) => [fixed, ...permutation]); // ���ƿ� ������ ���� �� ����(fixed) �� ���̱�
    results.push(...attached); // �迭 spread syntax �� ��δ� push
  });

  return results; // ��� ��� results return
};

const cal_switch = (s) => {
  let base = s[0];
  let cnt = 0;
  for (let c of s.slice(1)) {
    if (base != c) {
      base = c;
      ++cnt;
    }
  }
  return cnt;
};

const base_cnt = arr
  .map((el) => cal_switch(el))
  .reduce((acc, curr) => acc + curr, 0);
// console.log(base_cnt);

const new_arr = arr.map((el) => el[0] + el[el.length - 1]);
// console.log(new_arr);

const ans = getPermutations(new_arr, n).reduce((acc, curr) => {
  let cnt = base_cnt;

  for (let i = 0; i < n - 1; ++i) {
    if (curr[i][1] != curr[i + 1][0]) ++cnt;
  }
  return Math.min(acc, cnt);
}, 1000);

console.log(ans);
