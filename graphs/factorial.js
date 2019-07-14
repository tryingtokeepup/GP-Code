// OKay, so what is factorial?
// 10! = 10* 9!
// 9! = 9* 8!
// n! = n(n-1)!

function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

function factorial_iterative(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  current_sum = n;

  for (i = 1; i < n; i++) {
    // 10 * 9 * 8

    current_sum = current_sum * (n - i);
  }
  return current_sum;
}

console.log(factorial(5));

console.log(factorial_iterative(5));
