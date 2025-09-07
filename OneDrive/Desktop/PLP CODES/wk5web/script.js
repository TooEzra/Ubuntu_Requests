// Part 1: Mastering JavaScript Basics
// Variable declarations and conditionals
let userAge = 0;
function checkAge() {
    userAge = parseInt(document.getElementById('ageInput').value);
    let message = '';
    if (userAge >= 18) {
        message = 'You are an adult!';
    } else {
        message = 'You are a minor!';
    }
    document.getElementById('result').innerText = message;
}

// Part 2: JavaScript Functions – The Heart of Reusability
// Function to calculate total
function calculateTotal(a, b) {
    return a + b;
}

// Function to toggle content visibility
function toggleContent() {
    const content = document.getElementById('dynamicContent');
    if (content.style.display === 'none') {
        content.style.display = 'block';
    } else {
        content.style.display = 'none';
    }
}

// Part 3: JavaScript Loops – Embrace the Power of Repetition!
// Loop to populate list with numbers
function populateList() {
    const ul = document.getElementById('list');
    ul.innerHTML = '';
    for (let i = 1; i <= 5; i++) {
        const li = document.createElement('li');
        li.textContent = `Item ${i}`;
        ul.appendChild(li);
    }
}
populateList();

// While loop for countdown
let count = 3;
while (count > 0) {
    console.log(`Countdown: ${count}`);
    count--;
}

// Part 4: Mastering the DOM with JavaScript
// DOM interaction 1: Change title on click
document.getElementById('title').addEventListener('click', function() {
    this.textContent = 'JavaScript Rocks!';
});

// DOM interaction 2: Change result color
document.getElementById('result').addEventListener('mouseover', function() {
    this.style.color = 'blue';
});

// DOM interaction 3: Add new paragraph
document.getElementById('result').addEventListener('mouseout', function() {
    const p = document.createElement('p');
    p.textContent = 'Mouse left the result!';
    document.body.appendChild(p);
});