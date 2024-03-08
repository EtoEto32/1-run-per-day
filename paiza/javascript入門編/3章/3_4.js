process.stdin.resume();
process.stdin.setEncoding('utf8');

var count = 0;
while (count < 6) {
    console.log(count);
    count++;
}

for (var count2 = 0; count2 < 6; count2++) {
    console.log(count2);
}
var count3=0
for (count3 = 5; count3 < 11; count3++) {
    console.log(count3);
}

// 「ハローpaizaラーニング」を10回表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');

for(var s=0;s<10;s++){
    console.log("ハローpaizaラーニング")
}

// 数値を0から15まで表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');


for(var s=0;s<=15;s++){
    console.log(s)
}

// 1月から12月まで表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');

for(var s=1;s<=12;s++){
    console.log(s+"月")
}
