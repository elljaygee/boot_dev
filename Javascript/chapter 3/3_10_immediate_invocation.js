const total = (function calculateTotal(numMessages, bytesPerMessage) {
  return numMessages * bytesPerMessage;
})(100, 24);

// don't touch below this line

console.log("Total message cost:", total);

// example of immediate invocation:
// 
// const result = (function (a, b) {
//   return a + b;
// })(1, 2);

// console.log(result);