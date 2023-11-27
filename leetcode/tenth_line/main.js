const readline = require('readline');
const fs = require('fs');

const rl = readline.createInterface(
    {
        input: fs.createReadStream('./tenth_line/notes.txt'),
    }
);
let l = 1;
rl.on('line', (input) => {
    if (l === 10)
        console.log(`${input}`);
    l++;
})

rl.on('close', () => {
    // console.log("");
})
