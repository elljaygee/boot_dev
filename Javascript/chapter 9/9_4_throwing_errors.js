const sendMessage = (msg) => {
  if (msg.length > 70) {
    throw new Error("Message is too long");
  }
  else {
    return msg;
  }
};

export { sendMessage };
