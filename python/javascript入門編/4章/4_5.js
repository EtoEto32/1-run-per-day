process.stdin.resume();
process.stdin.setEncoding('utf-8');
// Your code here!

var team = ["勇者", "戦士", "魔法使い", "忍者"];
console.log(team);
console.log(team[0]);
for(var index=0;index<team.length;index++){
    console.log(team[index]);
}
for(var index in team){//for inを使う場合初期化宣言はいらない
    console.log(index);
}
for (var value of team) {//for ofを使う場合初期化宣言はいらない
    console.log(value);
}
//- 配列名.lengthで配列の長さがわかるので、繰り返し条件に指定できる
// `for (var 変数名 in 配列名) {`で配列に存在するすべてのインデックスを取得できる
//- [!] 必ずしも0から順番に取得できるとは限らない

//- `for (var 変数名 of 配列名) {`で配列の要素をすべて取得できる
//- ECMA Scriptが使える環境でのみ可能

// 配列の中身を1行ずつ表示してみよう

process.stdin.resume();
process.stdin.setEncoding('utf-8');

var enemy = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"];

// for文で配列の要素を1つずつ出力する
for(var index in enemy){
    console.log(enemy[index]);
}


