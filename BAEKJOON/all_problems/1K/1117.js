const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);

const [w, h, f, c, x1, y1, x2, y2] = inputData;
// console.log(w, h, f, c, x1, y1, x2, y2);

let colored_area = BigInt(
  Math.max(0, Math.min(x2, f) - x1) + Math.max(0, Math.min(x2, w - f) - x1)
);
colored_area *= BigInt((Math.min(h / (c + 1), y2) - y1) * (c + 1));

console.log((BigInt(w) * BigInt(h) - colored_area).toString());
