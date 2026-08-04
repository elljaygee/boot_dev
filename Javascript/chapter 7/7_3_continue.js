function printPrimes(max) {
  for (let n = 2; n <= max; n++) {
    let isPrime = true;
    if (n === 2){
      console.log(n);
      continue;
    }
    if (n % 2 === 0) {
      continue;
    }
    for (let i = 3; i * i <= n; i+=2) {
      if (n % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime === true){
      console.log(n);
    }
  }
}

// don't touch below this line

function test(max) {
  console.log(`Primes up to ${max}:`);
  printPrimes(max);
  console.log(
    "===============================================================",
  );
}

test(10);
test(20);
test(30);
