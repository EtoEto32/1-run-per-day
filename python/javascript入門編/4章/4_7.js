//- `split(",")`でカンマで区切って配列に変換できる
process.stdin.resume();
process.stdin.setEncoding('utf8');


var input_string = "";
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

reader.on('line', (line) => {
    input_string = line;
});

reader.on('close', () => {
    var values = input_string.split(",");
    console.log(values);

    for (var monster of values) {
        console.log(monster + "が現れた");
    }

    values.forEach(i1 => {
        console.log(i1 + "があらわれた");
    });

    for (var i2 in values) {
        console.log(values[i2] + "があらわれた");
    }

    for (var i3 = 0; i3 < values.length; i3++) {
        console.log(values[i3] + "があらわれた");
    }
});
/*aが現れた
hが現れた
fが現れた
aがあらわれた
hがあらわれた
fがあらわれた
aがあらわれた
hがあらわれた
fがあらわれた
aがあらわれた
hがあらわれた
fがあらわれた*/


// 文字列をカンマで分割してみよう

process.stdin.resume();
process.stdin.setEncoding('utf-8');

var team_str = "勇者,戦士,忍者,魔法使い";

// splitで分割し配列に格納、標準出力に出力する
var team = []; 
var team=team_str.split(",");//入れる先は配列
console.log(team);



// 文字列をカンマで分割してみよう

process.stdin.resume();
process.stdin.setEncoding('utf-8');

var input_string = "";
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

reader.on('line', (line) => {
    input_string = line;
});

reader.on('close', () => {
    var array = [];
    // ここでカンマで区切って配列に格納する
    array=input_string.split(",")
    console.log(array);
});