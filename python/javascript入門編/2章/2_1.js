// if文による条件分岐
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = 1;
if (number == 1) {
    console.log("スキ！"); // 条件式が成立したときの処理
} else {
    console.log("キライ");  // 条件式が成立しなかったときの処理
}

// if文による条件分岐
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = parseInt(Math.random() * 3) + 1;
console.log("あなたの順位は" + number + "位です");
// ここにif文を追加する
if(number==1){
    console.log("おめでとう")
    
}else if(number==2 | number==3){
    console.log("あと少し")
}//C言語に近いかも