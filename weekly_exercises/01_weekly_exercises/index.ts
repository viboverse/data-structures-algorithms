function twoSum(a: number, b: number): number {
  return a + b;
}

function sumOfArray(array: number[]): number {
  let res = 0;
  for (let i = 0; i < array.length; i++) {
    res += array[i];
  }

  return res;
}

console.log(sumOfArray([2, 5, 7]));
