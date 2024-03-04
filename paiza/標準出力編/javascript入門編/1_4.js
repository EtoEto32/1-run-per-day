// HTMLを表示する
process.stdin.resume();
process.stdin.setEncoding('utf8');
console.log("<h1>hello world</h1>");//<h1>hello world</h1>//htmlモードで大文字ブラウザ表示
console.log("<p>世界の皆さん、");
console.log("<b>こんにちは</b></p>");


process.stdout.write("<h1>hello world</h1>\n");//""\n"は改行コード
process.stdout.write("<p>世界の皆さん、\n");
process.stdout.write("<b>こんにちは</b></p>\n");

// HTMLを表示する
process.stdin.resume();
process.stdin.setEncoding('utf8');
console.log("<p>勇者は、荒野を歩いていた</p>");

// HTMLを表示する
process.stdin.resume();
process.stdin.setEncoding('utf8');
console.log("勇者は、荒野を歩いていた");
console.log("<b>モンスター</b>があらわれた");

