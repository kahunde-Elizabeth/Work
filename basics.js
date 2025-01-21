// a single line comment

/*MULTILINE COMMENT*/

//Variables can allow redifining the variables
var numberOne=3;

//const This is a value you dont want to change like pie in math
const numberTwo=5;

//let
let numberThree=9;

function checkLet(){
    let numberFour= 10;
    console.log(numberFour)
}
checkLet();

//datatypes
//datatype of string
let wordFirst="Hello World";
'',"",``
let firstName= "Kahunde";
let lastName= 'Liz';

let fullName=`Grace ${lastName}`;
console.log(fullName)
console.log(firstName.length);//Length of the string

//datatype of lists
let numberList=[1,2,34,7];
let numberListTwo=[9,8,7];
console.log(numberList+numberListTwo);

let fruitsList=["apples",'grapes', 'mangoes'];
fruitsList.push("banana");
console.log(fruitsList);

//datatype of boolean
let isStudent= true; 
let hasGraduated= false;
console.log(isStudent&&hasGraduated);// and logical operator
console.log(isStudent||hasGraduated);// or logical operator

//Datatype of Object
let personObject={
    "email": "kahunde@gmail.com",
    "gender": 'Female'
}
console.log(personObject);
//Arithmetic operations
console.log(numberTwo+numberTwo);
console.log(numberTwo*numberTwo);
console.log(numberTwo-numberTwo);
console.log(numberTwo/numberTwo);

let strOne='2';
let numOne=2;
console.log(strOne==numOne);
console.log(strOne===numOne)