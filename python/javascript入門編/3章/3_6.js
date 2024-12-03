//3_5が動画のみ

// これは、標準入力から整数を読み取り、それに100を加えて結果を標準出力に表示するシンプルなNode.jsスクリプトです。

// まず、標準入力から読み取りを再開します。
process.stdin.resume();
process.stdin.setEncoding('utf8');

// 入力を一時的に保存するための空の文字列を初期化します。
var input_string = "";

// 標準入力から行を読み取るためのreaderインターフェースを作成します。
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// 行が読み取られたときに実行されるコールバック関数です。
reader.on('line', (line) => {
    input_string = line;
});

// 入力ストリームが閉じられたときに実行されるコールバック関数です。
reader.on('close', () => {
    var input_int = parseInt(input_string);
    var result = input_int + 100;
    console.log(result);
});
/*標準入力の再開とエンコーディング設定:
process.stdin.resume();とprocess.stdin.setEncoding('utf8');は、標準入力を再開し、テキスト形式で読み取るための設定です。
入力を一時的に保存する変数:
input_stringは空の文字列で初期化されています。これは、入力を一時的に保存するための変数です。
標準入力から行を読み取るためのインターフェース作成:
require('readline').createInterfaceを使用して、標準入力から行を読み取るためのインターフェースを作成しています。
行が読み取られたときのコールバック関数:
reader.on('line', (line) => { ... });は、行が読み取られたときに実行されるコールバック関数です。読み取った行はinput_stringに格納されます。
入力ストリームが閉じられたときのコールバック関数:
reader.on('close', () => { ... });は、入力ストリームが閉じられたときに実行されるコールバック関数です。input_stringを整数に変換し、それに100を加えた結果を表示します。*/
// 標準入力からテキストを取得する

process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
reader.on('line', (line) => {
    lines.push(line);//pythonのappendみたいなもの
});
reader.on('close', () => {
    console.log("hello " + lines[0]);
    console.log("hello " + lines[1]);
    console.log("hello " + lines[2]);
});

/*これは、Node.jsスクリプトです。以下に解説をします。

process.stdin.resume();とprocess.stdin.setEncoding('utf8');は、標準入力を再開し、テキスト形式で読み取るための設定です。
linesは空の配列で初期化されています。これは、入力された行を一時的に保存するための変数です。
require('readline').createInterfaceを使用して、標準入力から行を読み取るためのインターフェースを作成しています。
reader.on('line', (line) => { ... });は、行が読み取られたときに実行されるコールバック関数です。読み取った行はlines配列に追加されます。
reader.on('close', () => { ... });は、入力ストリームが閉じられたときに実行されるコールバック関数です。lines[0]、lines[1]、lines[2]の内容を表示します。
このスクリプトは、ユーザーが入力した行を読み取り、それに対して処理を行う基本的なプログラムです。*/

// 複数行の標準入力を取得する

