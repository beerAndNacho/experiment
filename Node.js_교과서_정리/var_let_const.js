
var el = 0;
function test() {
    var el = 1;
    console.log(el);
}

console.log(el);

var el2 = 0;

{
    var el2 = 1;
    console.log(el2);
}

console.log(el2);

let el3 = 0;

{
    let el3 = 1;
    console.log(el3);
}

console.log(el3);

// var는 함수스코프를 갖고 let const는 블록 스코프를 갖는다.
// 이는 var는 함수 안에서만 어떤 특정한 범위를 갖고 
// 그 이외에는 특정한 범위 없이 전역에 영향을 미치게 될 수 있다.

// 반면 let과 const는 블록 스코프이므로 함수를 포함한 중괄호 형태의 내에서 범위를 따로 갖는다.