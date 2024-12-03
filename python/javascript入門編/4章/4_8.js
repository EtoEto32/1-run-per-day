//- `reader.on('line', (line) => {`の中で、配列に入力値をpushしていく
process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

reader.on('line', (line) => {
    lines.push(line);
});

reader.on('close', () => {
    for(var value of lines){
        console.log("hello"+value);
    }
});





process.stdin.resume();
process.stdin.setEncoding('utf-8');

var lines = [];
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

reader.on('line', (line) => {
    // 配列に標準入力を追加する
    lines.push(line);
});

reader.on('close', () => {
    // 配列の要素を繰り返し出力する
    for(var value of lines){
        console.log(value+"が現れた");
    }
});
