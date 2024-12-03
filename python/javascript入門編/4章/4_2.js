//4_1は配列についての動画

let i = 100;

for(let i=0; i<5; i++) {}

console.log(i); // 100
//for文の中で同じ変数名を使用しても、for文の外で宣言した変数には影響しません。
var j = 100;

for(var j=0; j<5; j++) {}

console.log(i); // 5
//varにはブロックスコープが無いのでfor文の中で同じ変数名を利用して宣言すると外で宣言した同じ変数名に影響がでます。

var k = 100;

function sample() {
 for(var k=0; k<5; k++) {}
}

console.log(k); // 100

//varは関数スコープなので関数内で宣言した変数は関数外で宣言した変数に影響しません。

process.stdin.resume();
process.stdin.setEncoding('utf-8');
// Your code here!

var player1="勇者";
var player2="魔法使い";
player1="戦士"
var team=["戦士","忍者",player2,"聖なる"+player1];
console.log(player1);
console.log(player2);
console.log(team);

// 配列の中身を出力してみよう

process.stdin.resume();
process.stdin.setEncoding('utf8');

var party = ["戦士", "侍", "僧侶", "魔法使い"];

// ここで配列を出力する
console.log(party);

// 指定の文字を配列にしてみよう

process.stdin.resume();
process.stdin.setEncoding('utf8');

// ここで配列を定義する
var item = ["ロングソード","ブレードソード","エクスカリバー"];

// ここで配列を出力する
console.log(item)

