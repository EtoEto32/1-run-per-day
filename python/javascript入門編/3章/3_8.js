process.stdin.resume();
process.stdin.setEncoding('utf8');

for(var seireki=1989;seireki<2019;seireki++){
    
    console.log("西暦"+seireki+"年");
    let heisei=seireki - 1988;//letは再び代入できない
    console.log("西暦"+seireki+"年は平成"+heisei+"年です");
}

// 西暦年と昭和年の対応表を作ろう
process.stdin.resume();
process.stdin.setEncoding('utf8');

for(let s=1926;s<1989;s++){
    wareki=s-1925
    console.log("西暦"+s+"年は昭和"+wareki+"年です")
}