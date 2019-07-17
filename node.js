function factorial(n) {
  // please dont give me negatives
  // if n is zero, or if n is 1, return 1
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5));

function factorial_iterative(n) {
  // 1,2,6
  counter = 1;
  for (i = 1; i <= n; i++) {
    counter = counter * i;
  }
  return counter;
}
console.log(factorial_iterative(5));
// (counter1 + counter2 * i +counter3 * (i+1) )
