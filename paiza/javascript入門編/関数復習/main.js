function message1() {//function 任意の関数名(引数){};
  console.log("Hello,Eisuke!");
};
message1();


//引数
function message2(userName) {//function 任意の関数名(引数){};
    console.log("こんにちは"+userName+"さん");//「+」を使って文字列を連結する
    console.log(`Hello,${userName}`);//「``」バッククォートを使うと変数を埋め込める `${変数名}`
};
message2("takashi");
message2("yoshiko");
message2("sachiko");

function calculation(x,y){
    //console.log(`number1は${x}です。number2は${y}です。`);
    const plus=x+y;
    const minus=x-y;
    console.log(`足し算の結果は${plus}です。引き算の結果は${minus}です。`);
};
calculation(5,10);
//変数・定数に関数を代入
const myFunc1=function myfunc1(userName) {//function 任意の関数名(引数){};
    console.log(`Hello,${userName}`);
};
myFunc1('田村');

//無名関数　関数を代入する場合にはこちらの方が一般的
const myfunc2=function(userName){
    console.log(`Hello,${userName}`);
};
myfunc2("山内");

//アロー関数
const myfunc3 = (userName)=>{ 
    console.log(`Hello,${userName}`);
};
myfunc3("田中");
//デフォルト引数
const greeting = (name,greet = "こんにちは") => {
    return[name,greet]
};
  
  console.log(greeting("太郎"))
  // =>["太郎", "こんにちは"]
  console.log(greeting("二郎"))
  // => ["二郎", "こんにちは"]
  console.log(greeting("三郎"))
  // => ["三郎", "こんにちは"]
  console.log(greeting("Jhon","Helllo"))
  // => ["Jhon", "Helllo"]
  console.log(greeting("chang","Ni Hao"))
  // => ["chang", "Ni Hao"]

//return
function add2(x,y){
    return x+y;
};

a=add2(3,4);//7
console.log(a);//7
console.log(add2(3,4));//7

function minus2(x,y){
    return x-y;
};
console.log(minus2(10,5));//5
console.log(minus2(10,add2(3,4)));//3

function myFunc4(){
    return;//returnで関数を抜ける(途中でも抜ける)
    console.log("myfunc4を実行しました");
};
myFunc4();