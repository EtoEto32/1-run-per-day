// if文による条件分岐 else if文
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = 1;
if (number == 1) {
  console.log("スキ！");// 条件式が成立したときの処理
} else if (number == 2) {
  console.log("どちらでもない");// 条件式2が成立したときの処理
} else {
  console.log("キライ");// 条件式がどちらも成立しなかったときの処理
}
//a == b	a と b が等しい	10 == 10
//a < b	a が b よりも小さい	10 < 15
//a > b	a が b よりも大きい	10 > 7
//a <= b	a が b 以下である	10 <= 15
//a >= b	a が b 以上である	10 >= 7
//a != b	a と b が等しくない	10 != 1

// if文による条件分岐　比較演算子
process.stdin.resume();
process.stdin.setEncoding('utf8');
var place = parseInt(Math.random() * 12) + 1;
process.stdout.write (place + "位");
// ここにif文を追加する
if (place<=6){
    console.log("入賞")
}else if(place>=7){
    console.log("入賞圏外")
}

