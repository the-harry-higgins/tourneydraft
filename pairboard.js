// const caesarCipher = (message, shift) => {
// 	if (!message.length) return message;

// 	const min = 'a'.charCodeAt(0);
//   const max = 'z'.charCodeAt(0);
//   shift %= 26;

// 	const arr = message.split('').map(letter => {
//     let value = letter.charCodeAt(0);
//     console.log(letter, value);
//     value = (value - min + shift) % (26) + min;
//     console.log(letter, value);

// 		return String.fromCharCode(value);
// 	});
// 	return arr.join('');
// }

// console.log(caesarCipher('abc', 3));
// console.log(caesarCipher('abc', 52));
// console.log(caesarCipher('xyz', 54));


const fib = (n, arr) => {
  if (arr[n]) return array[n];

  num = fib(n - 2) + fib(n - 1);
  array[n] = num;
  return num;
}

const fibsSum = (n) => {
  const array = Array.from(new Array(n));
  array[0] = 0;
  array[1] = 1;
  array[2] = 1;
  const lastVal = fib(n, array);
  const answer = array.reduce((s, i) => s + i) + lastVal;
  return answer;
}

console.log(fibsSum(1));
console.log(fibsSum(2));
console.log(fibsSum(3));
console.log(fibsSum(4));
console.log(fibsSum(5));