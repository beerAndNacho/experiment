// 블로킹 방식이다.
function longRunningTask() {
    // long time TASK
    console.log('작업 끝');
}

console.log('시작');

longRunningTask();

console.log('다음 작업 시작');

console.log('---------------------------------------');
// nonblocking으로 변경하면 다음과 같다.
function longRunningTask() {
    // long time TASK
    console.log('작업 끝');
}

console.log('시작');

setTimeout(longRunningTask, 0);
setImmediate(longRunningTask);

console.log('다음 작업 시작');

