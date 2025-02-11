// Q1
let name = "Wilson"; // String
let age = 30; // Number
let isStudent = true; // Boolean

console.log("Name:", name, "Type:", typeof name);
console.log("Age:", age, "Type:", typeof age);
console.log("Is Student:", isStudent, "Type:", typeof isStudent);

// Q2
let number = parseInt(prompt("Enter a number:"));

if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}

// Q3
let fruits = ["Durian", "Peach", "Strawberry", "Mango"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// Q4
function calculateArea(length, width) {
    return length * width;
}

let area = calculateArea(2, 10);
console.log("Area of rectangle:", area);