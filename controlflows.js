/**
 * IF STATEMENT
 */
/**if(condition){
    logic
} else if(condition){
    logic
}else{
    logic
}*/
//age, child,adult,invalid
let age=80
if(age<0){
    console.log("invalid")
}else if(age>=18){
    console.log('Adult')
}else{
    console.log('Child')
}


let number=5;
switch(number) {
    case 1:
        console.log('This is a Sunday');
        break;
    case 2:
        console.log('this is a Monday');
    case 3:
        console.log('This is a Tuesday')
         break;
    case 4:
        console.log('This is a Wednesday');
        break;
    case 5:
        console.log('This is a Thursday');
        break;
    case 6:
        console.log('This is a Friday');
        break;
    case 7:
        console.log('This is  a Saturday');
        break;
    default:
        console.log('This day doesnot exist')
        break;
}
// comparing passwords
let password='1234'
let confirmPasword='1234'
if(password== confirmPasword){
    console.log("Password is valid")
}
else{
    console.log("Password is not the same\n try Again")
}
//loops
//For Loops
/*for (intialization, condition, increment){
    results
}*/
for (let r=0; r<101;r+=1){
    console.log(r);
}
//While loop//infinte loop press control+c
let r=0;
while(r<101){
    console.log(r)
    r+=1;
}
//For in loop//Arrays
let fruitList=['apples','mangoes','oranges'];
for (fruit in fruitList){
    console.log(fruitList[fruit]);

}
//For of loop
for(fruit of fruitList){
    console.log(fruit);
}
