// if文による条件分岐 else if文
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = 1;
if (number == 1) {
    console.log("スキ！");// 条件式1が成立したときの処理
}else if(number == 2){
    console.log("どちらでもない");//条件式2が成立したときの処理
}else {
    console.log("キライ");//条件式がどちらも成立しなかったときの処理
}

// if文による条件分岐　else if文
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = parseInt(Math.random() * 5) + 1;
console.log("あなたの順位は" + number + "位です");
// ここにif文を追加する
if (number == 1) {
  console.log("おめでとう");
} else if (number == 2) {
  console.log("あと少し");
} else {
  console.log("よくがんばったね");
}

