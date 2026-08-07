function getPrimaryAndBackupMessages(messages) {
  let primary = undefined;
  let backups = [];
  if (messages.length == 0) {
    return {primary, backups}
  }
  [primary, ...backups] = messages;
  return {primary, backups}
}

export { getPrimaryAndBackupMessages };

/* BootDev solution:
function getPrimaryAndBackupMessages(messages) {
  const [primary, ...backups] = messages;
  return { primary, backups };
}

export { getPrimaryAndBackupMessages };
(destructuring an empty array [], attempting to extract the first element results in undefined and automatically assigns this to primary; the rest operator (...) always creates a brand new array containing any remaining elements, when applied to an empty array, there are zero remaining elements, so it defaults to an empty array [].)

import { describe, it, assert, withSubmit } from "./unit_test.js";
import { getPrimaryAndBackupMessages } from "./main.js";

describe("getPrimaryAndBackupMessages returns primary and backup messages correctly", () => {
  const runCases = [
    {
      messages: [
        "Welcome to Textio!",
        "Your order has shipped",
        "Reminder: Payment due soon",
      ],
      expected: {
        primary: "Welcome to Textio!",
        backups: ["Your order has shipped", "Reminder: Payment due soon"],
      },
    },
    {
      messages: ["First Message"],
      expected: { primary: "First Message", backups: [] },
    },
    {
      messages: [],
      expected: { primary: undefined, backups: [] },
    },
  ];

  const submitCases = runCases.concat([
    {
      messages: ["Alert", "Update", "Follow up", "Confirmation"],
      expected: {
        primary: "Alert",
        backups: ["Update", "Follow up", "Confirmation"],
      },
    },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ messages, expected }, i) => {
    it(`Test #${i}`, () => {
      const result = getPrimaryAndBackupMessages(messages);
      assert.deepEqual(result, expected);
    });
  });

  const numSkipped = submitCases.length - testCases.length;
  if (numSkipped > 0) {
    console.log(`- Skip: ${numSkipped} test case(s) for submit`);
  }
});
*/