const fs = require('fs');
const input_data = fs.readFileSync(0, 'utf-8').trim().split('\n').map(BigInt);

const max_line_num = input_data.length;
let line = 0;

while (line < max_line_num) {
  const n = parseInt(input_data[line]);
  //   console.log('n', n);

  let value = 0n;
  for (let line_index = 1; line_index <= n; ++line_index) {
    value += input_data[line + line_index];
  }
  //   console.log(value);

  if (value > 0n) {
    console.log('+');
  } else if (value == 0n) {
    console.log(0);
  } else {
    console.log('-');
  }

  line += n + 1;
}
