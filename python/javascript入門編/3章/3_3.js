process.stdin.resume();
process.stdin.setEncoding('utf8');

var hp = 30;
while (hp > 0) {
    let damage = Math.floor(Math.random() * 10);//ランダムダメージ数
    console.log("スライムに" + damage + "のダメージを与えた");
    hp -= damage;
}
console.log("スライムを倒した！");

/*nsole.log(Math.floor(5.95));
// Expected output: 5

console.log(Math.floor(5.05));
// Expected output: 5

console.log(Math.floor(5));
// Expected output: 5

console.log(Math.floor(-5.05));
// Expected output: -6*/


// 数値を10から1までカウントダウン表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');
var count=10;
while(count>0){// 20から10までの奇数を表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');

var count=20
while(count>=10){
    if(count%2==1)
        console.log(count)
        count-=1
}
    console.log(count);
    count-=1;
}

// 数値を20から10までカウントダウン表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');

var count=20
while(count>=10){
    console.log(count)
    count-=1
}
// 20から10までの奇数を表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');

var count=20
while(count>=10){
    if(count%2==1)
        console.log(count)
        count-=1
}

