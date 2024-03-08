// 1から10までの偶数を表示する

process.stdin.resume();
process.stdin.setEncoding('utf8');
var count=1;
while(11>count){
    if(count%2==0){
    console.log(count);
    }
    count+=1;
}
