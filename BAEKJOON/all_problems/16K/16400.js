const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf-8').trim().split().map(Number);
// console.log(inputData);
n = inputData[0];

sieve = [];
for (let i = 0; i <= n; ++i) {
  sieve[i] = true;
}

primes = [];
for (let i = 2; i <= n; ++i) {
  if (sieve[i]) {
    primes.push(i);
    for (let j = i * 2; j <= n; j += i) {
      sieve[j] = false;
    }
  }
}
// console.log(primes.length);

dp = [];
for (let i = 0; i <= n; ++i) dp[i] = 0;
dp[0] = 1;

for (let p of primes) {
  for (let i = p; i <= n; ++i) {
    dp[i] = (dp[i] + dp[i - p]) % 123456789;
  }
}

console.log(dp[n]);
