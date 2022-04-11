//for문과 async/await을 같이 써서 Promise.all을 대체할 수 도 있습니다.

const promise1 = Promise.resolve('성공1');
const promise2 = Pormise.resolve('성공2');

(async () => {
    for await (promise of [promise, promise2]) {
        console.log(promise);
    }
})


// 앞으로 중처보디는 콜백 함수가 있다면 프로미스를 거쳐 async/await 문법을 바꾸는 연습을 해야한다.
