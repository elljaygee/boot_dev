function calculateCampaignMetrics(sent, opened, clicked) {
  const openRate = opened / sent;
  const clickRate = clicked / sent;
  const conversionRate = clicked / opened;
  return {
    openRate,
    clickRate,
    conversionRate,
  };
}

// don't touch above this line
// destructure the object created in the above function and assign the values to the named variables
const { openRate, clickRate, conversionRate } = calculateCampaignMetrics(1000, 800, 200);

// don't touch below this line

console.log(`Open Rate:       ${openRate}`);
console.log(`Click Rate:      ${clickRate}`);
console.log(`Conversion Rate: ${conversionRate}`);
