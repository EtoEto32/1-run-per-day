// RPGのクリティカルヒットを再現
// 比較演算子 == > < >= <= !=

// スライムと戦っている。
// 1から10の目のサイコロをふって、
// 6未満：サイコロの目だけダメージを与えたと表示。
// 6以上：クリティカルヒットとして、100のダメージを与えたと表示。
process.stdin.resume();
process.stdin.setEncoding('utf8');
var hit=parseInt(Math.random()*10)+1;
//console.log(hit);

if(hit<6){
    console.log("スライムに、"+hit+"のダメージを与えた!");
}else{
    console.log("クリティカルヒット!スライムに、100のダメージを与えた!");
}


process.stdin.resume();
process.stdin.setEncoding('utf8');
var dice = parseInt(Math.random() * 6) + 1;
console.log("サイコロは" + dice);
if(dice>=4){
    console.log("スライムの攻撃をかわした")
}else{
    console.log("スライムから10のダメージを受けた")
}
