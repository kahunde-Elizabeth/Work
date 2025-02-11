//Synchronous
//Step one
/*console.log("Boiling the water")

//Step Two
console.log('Water is ready')
//Step Three
console.log('Do other things')
*/

//Asynchronous
console.log("Boiling the water")

setTimeout(()=>{
    console.log('Water is ready');
},4000);
console.log('Do other things')
