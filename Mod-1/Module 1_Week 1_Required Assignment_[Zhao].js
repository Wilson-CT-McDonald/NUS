// Assignment 1 - ZHAO CHENTONG

Q1
var x = 10; // Declare var X and assign 10
var y = "Hello"; // Declare var Y and assign 'Hello'
var result = y + " " + x; // Concatenate var X and Y and store them in var result
console.log(result); // Print the output

Q2
// Declare function to check if is even or odd number
function checkEvenOdd(number) { 
	// Check if the number is even by checking if is divisible by 2
	if (number % 2 === 0) {
		// Print out "Even"
		console.log("Even");
	}
	// if its not even, then it must be odd
	else {
		// Print out "Odd"
		console.log("Odd");
	}
}
// Example
checkEvenOdd(4);
checkEvenOdd(3);

Q3
// Declare function to take in parameter 'name'
function greetUser(name) {
	// print "Hello, [name]!" to the console
	console.log("Hello, " + name + "!");
}
// Example
greetUser("Alice");  // Output: "Hello, Alice!"
greetUser("Bob");    // Output: "Hello, Bob!"
greetUser("Charlie"); // Output: "Hello, Charlie!"

Q4
<html>
// Title
<head>
	<title>My Webpage</title>	
</head>
// Body
<body>
	// Heading
	<h1>Welcome to My Webpage</h1>
	// Paragraph
	<p>
		This webpage is created by Zhao Chentong to demostrate a simple HTML.
		It contains a title, a heading, a paragraph of brief description on the page and an unordered list below that includes 3 of my hobbies.
	</p>
	// Unordered list with 3 of my hobbies
	<ul>
		<li>Texas Poker</li>
		<li>Cooking</li>
		<li>Badminton</li>
	</ul>
</body>
</html>
