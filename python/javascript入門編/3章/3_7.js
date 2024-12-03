process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
reader.on('line', (line) => {
    // ここで入力を処理する
    lines.push(line);
});
reader.on('close', () => {
    // ここで出力する
    console.log(lines[0]);
    console.log(lines[1]);
    console.log(lines[2]);



});
