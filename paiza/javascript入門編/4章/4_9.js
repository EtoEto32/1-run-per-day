//- `Math.random()`で0〜1未満のランダムな数が生成できる
//- `Math.floor()`で小数点以下切り捨て
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

    for (var monster of values) {
        console.log(monster + "があらわれた");
    }

    // 生成するランダムな数値の範囲を調べる
    var number_of_monsters = values.length;
    console.log("モンスターが" + number_of_monsters + "匹あらわれた");

    // ランダムにインデックスを生成する
    var target = Math.floor(Math.random() * number_of_monsters);
    console.log(target);

    // 選ばれた一匹に会心の一撃を繰り出す
    console.log(values[target] + "に会心の一撃！モンスターを倒した");
});

// じゃんけんプログラムを作ろう

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

    // 配列をそのまま出力する
    console.log(values);
    // 生成するランダムな数値の範囲を調べる
    var number=values.length;
    // ランダムにインデックスを生成する
    var target =Math.floor(Math.random()*number)
    // 選ばれた手を出力する
    console.log(values[target])

});
