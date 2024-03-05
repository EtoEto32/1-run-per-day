// 数の表示とサイコロ
process.stdin.resume();
process.stdin.setEncoding('utf8');
var randnum=parseInt(Math.random()*10)+1;//Mathは最初大文字 0～10のランダムな数字
//そのままでは絶対10は表示されないし(0から数えるから)、0が出てしまう
//だから最後に1を足す
//console.log(randnum);

//var number = 300;
console.log("スライムが"+randnum+"匹現れた");




// 数の表示とサイコロ
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = parseInt(Math.random() * 6) + 1;
var str1="サイコロの目は"
var str2="です"

console.log(str1+number+str2);
