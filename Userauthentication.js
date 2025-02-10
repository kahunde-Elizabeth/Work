


const fs=require('fs')
const readline=require('readline');
let rl =readline.createInterface(process.stdin,process.stdout);

function userCredentials(){
    rl.question('Enter username',(username)=>{
        rl.question('Enter password',(password)=>{
            rl.question('Enter email',(email)=>{
                
                const crudentials={username,password,email};
                console.log(`Username:${username}`);
                console.log(`Password:${password}`);
                console.log(`Email:${email}`);
                fs.writeFile('storage.json',JSON.stringify(crudentials),(err)=>{
                    if (err)console.error('error in saving the file',err);
                    else console.log('Crundentials saved successfully');
                    rl.close()
                })
            })
        })
    })
}

function promptUserCredentials() {
    rl.question('Enter email: ', (email) => {
        rl.question('Enter password: ', (password) => {
            verifyCredentials(email, password);
        });
    });
}


function verifyCredentials(email, password) {
    fs.readFile('storage.json', 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the file', err);
            rl.close();
            return;
        }

        const storedCredentials = JSON.parse(data);
        if (storedCredentials.email === email) {
            if (storedCredentials.password === password) {
                console.log('Access granted');
                displayMenu(storedCredentials);
            } else {
                console.log('Access denied: Incorrect password');
            }
        } else {
            console.log('Access denied: Email not found');
        }
        rl.close();
    });
}

function displayMenu(user) {
    console.log('\nUser Menu:');
    console.log('1. View Profile');
    console.log('2. Logout');
    console.log('3. Exit');
    rl.question('Choose an option: ', (option) => {
        switch (option) {
            case '1':
                console.log(`\nProfile:\nUsername: ${user.username}\nEmail: ${user.email}`);
                displayMenu(user);
                break;
            case '2':
                console.log('Logged out successfully');
                rl.close();
                break;
            case '3':
                console.log('Exiting...');
                rl.close();
                break;
            default:
                console.log('Invalid option. Please try again.');
                displayMenu(user);
                break;
        }
    });
}

userCredentials()