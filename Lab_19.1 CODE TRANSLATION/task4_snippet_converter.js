// Task 4 (JavaScript): Equivalent filter & map snippet
const users = [
  { name: "Ansika", active: true, score: 95 },
  { name: "Vikram", active: false, score: 70 },
  { name: "Neha", active: true, score: 88 },
];
const topActive = users
  .filter((u) => u.active)
  .map((u) => `${u.name}: ${u.score}`);
console.log("Active:", topActive);
