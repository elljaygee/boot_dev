class Message {
  static numMessages = 0;
  static totalLength = 0;
  
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
    Message.numMessages++;
    Message.totalLength += body.length;
  }
  static getAverageMessageLength() {
    let average = Message.totalLength / Message.numMessages;
    return Math.round(average * 100) / 100;
  }
}

// don't touch below this line

export { Message };

/*
import { describe, it, assert, withSubmit } from "./unit_test.js";
import { Message } from "./main.js";

describe("Message", () => {
  const runCases = [
    {
      messages: [
        {
          recipient: "555-1111",
          sender: "555-2222",
          body: "For the Ancients!",
        },
        {
          recipient: "555-3333",
          sender: "555-4444",
          body: "The spirit moves me!",
        },
        { recipient: "555-5555", sender: "555-6666", body: "To battle!" },
      ],
      expected: {
        averageLength: 15.67,
      },
    },
    {
      messages: [
        {
          recipient: "555-7777",
          sender: "555-8888",
          body: "I bring the fire.",
        },
        {
          recipient: "555-9999",
          sender: "555-0000",
          body: "Let's shake things up!",
        },
      ],
      expected: {
        averageLength: 17.2,
      },
    },
  ];

  const submitCases = runCases.concat([
    {
      messages: [
        { recipient: "555-1234", sender: "555-5678", body: "Time to bash!" },
        {
          recipient: "555-9876",
          sender: "555-4321",
          body: "You play with fire!",
        },
      ],
      expected: {
        averageLength: 16.86,
      },
    },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ messages, expected }, i) => {
    it(`Test ${i}`, () => {
      messages.forEach(({ recipient, sender, body }) => {
        new Message(recipient, sender, body);
      });

      const averageLength = Message.getAverageMessageLength();
      assert.strictEqual(averageLength, expected.averageLength);
    });
  });

  const numSkipped = submitCases.length - testCases.length;
  if (numSkipped > 0) {
    console.log(`- Skip: ${numSkipped} test case(s) for submit`);
  }
});
*/