process.stdin.resume();
process.stdin.setEncoding('utf8');

// 条件式に使う変数の初期化処理
var count = 0;
while (count < 6) {
    // 繰り返し処理
    console.log(count);
    // 条件式に使う変数の値の更新
    count = count + 1;
}
console.log("last:" + count);


// 「ハローpaizaラーニング」と10回表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');
var count=0
while(count<10){
    console.log("ハローpaizaラーニング")
    count+=1
    
}

// 数値を0から15まで表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');


var count=0
while(count<=15){
    console.log(count)
    count+=1
}