const user = {
  name: "Default User",
  type: "user",
};

const adminUser = Object.create(user);
adminUser.type = "admin";

// checking the prototype chain of each user type
const isAdmin = function (userObject) {
  if (Object.getPrototypeOf(userObject) === adminUser) {
    return true;
  }  
  return false;
};

// don't touch below this line

export { user, adminUser, isAdmin };

/*
import { describe, it, assert, withSubmit } from "./unit_test.js";
import { user, adminUser, isAdmin } from "./main.js";

describe("Prototype Chains and isAdmin function", () => {
  const runCases = [
    {
      testType: "admin instance 1",
      userObject: Object.create(adminUser),
      expectedResult: true,
    },
    {
      testType: "admin instance 2",
      userObject: Object.create(adminUser),
      expectedResult: true,
    },
    {
      testType: "regular user",
      userObject: Object.create(user),
      expectedResult: false,
    },
    {
      testType: "object not linked to prototype chain",
      userObject: { type: "admin" },
      expectedResult: false,
    },
  ];

  const submitCases = runCases.concat([
    {
      testType: "admin user object itself",
      userObject: adminUser,
      expectedResult: false,
    },
    {
      testType: "wrong admin-like prototype",
      userObject: Object.create({ type: "admin" }),
      expectedResult: false,
    },
    {
      testType: "indirect admin descendant",
      userObject: Object.create(Object.create(adminUser)),
      expectedResult: false,
    },
  ]);

  let testCases = runCases;
  if (withSubmit) {
    testCases = submitCases;
  }

  testCases.forEach(({ testType, userObject, expectedResult }) => {
    it(`should return ${expectedResult} for ${testType}`, () => {
      const result = isAdmin(userObject);
      assert.strictEqual(result, expectedResult);
    });
  });

  const numSkipped = submitCases.length - testCases.length;
  if (numSkipped > 0) {
    console.log(`- Skip: ${numSkipped} test case(s) for submit`);
  }
});
*/
