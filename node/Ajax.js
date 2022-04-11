// 페이지 전환 없이 새로운 데이터를 불러오는 사이트는 대부분 AJAX 기술을 사용하고 있다.
// 보통 AJAX 요청은 jQuery나 axios  같은 라이브러리를 이용해서 보낸다.

// var xhr = new XMLHttpRequest();
// xhr.open
// xhr.onreadysataechange는 이벤트 리스너로 요청한 후 서버로부터 응답이 올 때 응답 받을 수 있다.

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
    if (xhr.readyState === xhr.DONE) {
        if(xhr.status === 200 || xhr.status === 201) {
            console.log(xhr.responseText);

        } else {
            console.error(xhr.responseText);
        }
    }
};

xhr.open('GET', 'https://www.naver.com');
xhr.send();

//
var xhr = new XMLHttpRequest();
var data = {
    name :"",
    birth:""

}
xhr.onreadystatechange = function() {
    if (xhr.readState === xhr.DONE) {
        if(xhr.readyState === 200 || xhr.status === 201) {
            console.log(xhr.responseText);
        } else {
            console.error(xhr.responseText);
        }
    }
};

xhr.open('POST', 'https://www.zerocho.com/api/post/json');
xhr.setRequestHeader('Content-Type', 'application/json') // 콘텐츠 타입을 json
xhr.send(JSON.stringify(data));