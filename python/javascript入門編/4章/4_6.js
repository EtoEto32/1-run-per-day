process.stdin.resume();
process.stdin.setEncoding('utf-8');
// Your code here!

var team = ["勇者", "戦士", "魔法使い"]

for (var value of team) {
    console.log(value);
}

team.forEach(value => {//Each、それぞれ、各々
    console.log(value);
});

//- `配列名.forEach(変数名 => {`で配列の要素を一つずつ取り出すことができる(昇順)
//- => は「アロー関数」

// forEachで配列の要素を出力してみよう
process.stdin.resume();
process.stdin.setEncoding('utf-8');

var cities = ["Tokyo", "Kanagawa", "Chiba", "Shizuoka", "Saitama"];


// forEachで配列の要素を1行ずつ出力する

cities.forEach(val=>{
    console.log(val);
});
/*
ECMAScriptとは、国際的な標準化団体のEcma International（エクマ・インターナショナル）が策定しているJavaScriptの標準規格。 
ECMA-262として規格書が発行されており、同様のものがISO/IEC 16262やJIS X 3060としても標準化されている。
*/