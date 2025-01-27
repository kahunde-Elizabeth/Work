//two types
//-void functions
//-Returning functions
/*function addition(numberOne, numberTwo){
    return numberOne + numberTwo;
}
//void
function sum (numberOne, NumberTwo){
    let summation=numberOne+NumberTwo;
    console.log(summation)
}
sum(6,8);//for void functions
console.log(addition(32,57));// for returning functions

//Arrow functions
const subtraction=(numberOne,numberTwo)=>{
    return numberOne-numberTwo;
}
const difference=(numberOne, numberTwo) =>{
    console.log(`The difference is ${numberOne-numberTwo}`)
}
console.log(subtraction(67,32))
difference(99,67)

function welcome(name){
    console.log(`Welcome to Moodle ${name}`);
}
welcome("Teddy");*/

let firstName='John';//Global variable
function welcome(name){
    console.log(`Welcome to Moodle ${name}`);
}

welcome(firstName);


const welcome=()=>{
    let firstName="JANE";//local variable
    console.log(`Welcome to moodle ${firstName}`)
}
welcome();

