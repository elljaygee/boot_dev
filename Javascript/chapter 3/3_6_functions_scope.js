function getMessageStatus(message) {
  let messageStatus = "processing";

  function isValidLength(message) {
    let messageStatus = "invalid";

    if (message.length > 0) {
      messageStatus = "valid";
    }

    return messageStatus;
  }

  // don't touch above this line

  return isValidLength(message);

}

// don't touch below this line

export { getMessageStatus };

/*
import { describe, assert, it, withSubmit } from "./unit_test.js";
import { getMessageStatus } from "./main.js";

describe("getMessageStatus", () => {
  const runCases = [
    { message: "Tread lightly.", expected: "valid" },
    { message: "Jesse, we need to cook!", expected: "valid" },
    { message: "", expected: "invalid" },
  ];

  const submitCases = runCases.concat([
    { message: "I am the danger", expected: "valid" },
    { message: " Say my name  ", expected: "valid" },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ message, expected }) => {
    it(`should return "${expected}" for message "${message}"`, () => {
      assert.strictEqual(getMessageStatus(message), expected);
    });
  });

  const numSkipped = submitCases.length - testCases.length;
  if (numSkipped > 0) {
    console.log(`- Skip: ${numSkipped} test case(s) for submit`);
  }
});
*/