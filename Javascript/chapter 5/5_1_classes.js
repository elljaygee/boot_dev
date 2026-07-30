/*
The class declaration creates a new class
The constructor method is a special method that's called when a new instance of the class (object) is created
The new keyword calls the constructor method and creates a new instance of the class
e.g:
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const user = new User("Lane", 100);
*/

class Message {
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
  }
}

// don't touch below this line

export { Message };

/*
import { describe, assert, it, withSubmit } from "./unit_test.js";
import { Message } from "./main.js";

describe("Message", () => {
  const runCases = [
    {
      recipient: "555-1234",
      sender: "555-5678",
      body: "Live long and prosper!",
      expected: {
        recipient: "555-1234",
        sender: "555-5678",
        body: "Live long and prosper!",
      },
    },
    {
      recipient: "555-9876",
      sender: "555-4321",
      body: "Boldly go where no man has gone before.",
      expected: {
        recipient: "555-9876",
        sender: "555-4321",
        body: "Boldly go where no man has gone before.",
      },
    },
  ];

  const submitCases = runCases.concat([
    {
      recipient: "555-1111",
      sender: "555-2222",
      body: "Things are only impossible until they're not",
      expected: {
        recipient: "555-1111",
        sender: "555-2222",
        body: "Things are only impossible until they're not",
      },
    },
    {
      recipient: "555-3333",
      sender: "555-4444",
      body: "Beam me up, Scotty.",
      expected: {
        recipient: "555-3333",
        sender: "555-4444",
        body: "Beam me up, Scotty.",
      },
    },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ recipient, sender, body, expected }, i) => {
    it(`Test ${i}`, () => {
      const result = new Message(recipient, sender, body);
      for (const prop of Object.keys(expected)) {
        assert.strictEqual(
          result[prop],
          expected[prop],
          `expected property "${prop}" to be: ${expected[prop]}, got: ${result[prop]}`,
        );
      }
    });
  });

  const numSkipped = submitCases.length - testCases.length;
  if (numSkipped > 0) {
    console.log(`- Skip: ${numSkipped} test case(s) for submit`);
  }
});
*/