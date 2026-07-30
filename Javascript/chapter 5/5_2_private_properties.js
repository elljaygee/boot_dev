class Message {
  // set createdAt as a private property, meaning it can't be accessed or modified from outside the class
  #createdAt;
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
    this.#createdAt = new Date();
  }
}

// don't touch below this line

const message = new Message("555-1234", "555-5678", "Hi there!");

console.log("Attempting to access the property createdAt...");
console.log("createdAt: " + message.createdAt);

const messageClass = Message.toString();
console.log("has private createdAt: " + messageClass.includes("#createdAt"));
