// 計算する
process.stdin.resume();
process.stdin.setEncoding('utf8');
var number = 10%3;
console.log(number);
console.log("西暦" + (2000 + 5 )+ "年")//西暦2005年
/*"西暦" + 2000 + 5 + "年"

の結果は"西暦20005年"になります。なぜでしょうか？
これは、演算の優先順位が同じ場合は左から計算がされるためです。

まず”西暦" + ”2000”で文字列が結合して”西暦2000”という文字列になり、
次に”西暦2000” + "5"で文字列が結合して”西暦20005”になります。
そして最後に"西暦20005"+"年"で”西暦20005年”になるわけです。*/


//演算子はpythonと一緒
// 計算する
process.stdin.resume();
process.stdin.setEncoding('utf8');
var a = 31;
var b = 17;
// 以下に、aとbをかけ算し、結果を出力するコードを書く
console.log(a*b)

// 計算する
process.stdin.resume();
process.stdin.setEncoding('utf8');
var x = 8;
var y = 5;
// 以下に、xをyで割ったときの余りを計算し、結果を出力するコードを書く
console.log(x%y)