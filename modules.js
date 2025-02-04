//.fs
const {fs}= require ('fs');

fs.writeFile('code.txt','Hello world',(error)=>{
    if(error) throw error;
    console.log('The file is created.')
})
fs.appendFile('code.txt','\n  this is line Two',(error)=>{
    if (error) throw error;
    console.log('The text is added.')
})
fs.readFile('code.txt-','utf8',(err,data)=>{
    if(err) throw err
    console.log(data)
})
// Path
const path= require('path')
let fullpath= path.join(__dirname, "code.txt")
console.log(fullpath);
//os
const os = require('os')
console.log(`the free space i have is${os.freemem()}`);