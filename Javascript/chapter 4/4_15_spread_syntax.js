function mergeTemplates(defaultTemplates, customTemplates) {
  return {...defaultTemplates, ...customTemplates}
}
// spread syntax shallow-copies the properties of the objects you're spreading. If properties have the same name, the last (right-most) object's property will overwrite the previous ones.  If different, they will be merged together into one object.

// don't touch below this line

export { mergeTemplates };

/*
import { describe, it, assert, withSubmit } from "./unit_test.js";
import { mergeTemplates } from "./main.js";

describe("mergeTemplates", () => {
  const runCases = [
    {
      defaultTemplates: {
        welcome: "Welcome to Textio! Start sending messages today.",
        support: "Need help? Contact our support team.",
      },
      customTemplates: {
        promo: "Limited time offer! Sign up now.",
        support: "Reach out to us for exclusive deals.",
      },
      expected: {
        welcome: "Welcome to Textio! Start sending messages today.",
        support: "Reach out to us for exclusive deals.",
        promo: "Limited time offer! Sign up now.",
      },
    },
    {
      defaultTemplates: {
        onboarding: "Here's how to get started with Textio.",
      },
      customTemplates: {
        promo: "Limited time offer! Sign up now.",
      },
      expected: {
        onboarding: "Here's how to get started with Textio.",
        promo: "Limited time offer! Sign up now.",
      },
    },
  ];

  const submitCases = runCases.concat([
    {
      defaultTemplates: {
        welcome: "Welcome to Textio! Start sending messages today.",
      },
      customTemplates: {
        welcome: "Welcome back to Textio!",
      },
      expected: {
        welcome: "Welcome back to Textio!",
      },
    },
    {
      defaultTemplates: {},
      customTemplates: {
        promo: "Limited time offer! Sign up now.",
      },
      expected: {
        promo: "Limited time offer! Sign up now.",
      },
    },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ defaultTemplates, customTemplates, expected }, i) => {
    it(`Test ${i}`, () => {
      const result = mergeTemplates(defaultTemplates, customTemplates);
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