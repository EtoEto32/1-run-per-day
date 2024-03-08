process.stdin.resume();
process.stdin.setEncoding('utf8');
// Your code here!

var team = ["勇者", "戦士", "魔法使い"];
console.log(team);

console.log(team[0]);
console.log(team[1]);
console.log(team[2]);

var index = 0;
console.log(team[100]);//undefined

// 配列の最初の要素を取り出してみよう

process.stdin.resume();
process.stdin.setEncoding('utf8');

team = ["勇者", "戦士", "侍", "忍者", "魔法使い"];

// ここで最初の要素を出力する
console.log(team[0]);
