// 西暦年から平成年を求める
process.stdin.resume();
process.stdin.setEncoding('utf8');
var today=new Date();
var seireki=today.getFullYear();
process.stdout.write("西暦"+seireki+"年は、");
//平成1年とは、西暦1989年。その差は1988
//西暦年-1988=平成*年
//例：西暦1989年-1988=平成1年
//例：西暦2015年-1988=平成27年
var heisei=seireki-1988;
console.log("平成"+heisei+"年です。");

// 西暦年から昭和年を求める
process.stdin.resume();
process.stdin.setEncoding('utf8');
var seireki = parseInt(Math.random() * 63) + 1926;
process.stdout.write ("西暦" + seireki + "年は");

// 昭和年を計算
var showa = seireki-1925;
console.log("昭和" + showa + "年です");