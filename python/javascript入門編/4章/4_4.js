process.stdin.resume();
process.stdin.setEncoding('utf8');
// Your code here!

var team = ["勇者", "戦士", "魔法使い"];

team[3] = "遊び人";//配列の対象外にならない。

team[team.length] = "商人";//配列の長さ team.length=3
team.push("狩人");//- `配列名.push(要素)`で末尾に要素を追加できる

team[1] = "格闘家";//上書き

team[100] = "王様";

console.log(team);
console.log(team[0]);
console.log(team.length);
/*
[ '勇者', '格闘家', '魔法使い', '遊び人', '商人', '狩人', <94 empty items>, '王様' ]
勇者
101
*/


// 配列に要素を追加してみよう

process.stdin.resume();
process.stdin.setEncoding('utf-8');

var weapon = ["木の棒", "鉄の棒", "鉄の剣", "鋼の剣"];

// ここで要素を追加する
weapon[weapon.length]="石斧"

console.log(weapon);

// 配列の要素を上書きしてみよう

process.stdin.resume();
process.stdin.setEncoding('utf-8');

var weapon = ["木の棒", "鉄の棒", "鉄の剣", "鋼の剣"];

// ここで配列の要素を上書きする
weapon[3]="石斧"

console.log(weapon);
