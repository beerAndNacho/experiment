const condition = true;
const promise   = new Promise((resolve, reject) => {
    if(condition) {
        resolve('성공');
    } else {
        reject('실패');
    }
})

// promise.then((message) => {
//     console.log(message);
// })
// .catch((error) => {
//     console.error(error);
// })


//


promise.then((message) => {
    return new Promise((resolve, reject) => {
        resolve(message);
    });
})
.then((message2) => {
    console.log(message2);
    return new Promise((resolve, reject) => {
        resolve(message2)
    })
})
.then((message3) => {
    console.log(message3);
})
.catch((error) => {
    console.error(error);
})



// 프로미스 활용 방법
// function findAndSaveUser(Users) {
//     Useres.findOne({}, (err, user) => {
//         if(err) {
//             return console.error(err);
//         }

//         user.name = 'zero';
//         user.save((err) => {
//             if(err) {
//                 return console.error(err);;
//             }

//             Users.findOne({gender:'M'},(err, user) => {
//                 //생량
//             })
//         })
//     })
// }



const promise1 = Promise.resolve('성공1');
const promise2 = Pormise.resolve('성공2');

Promise.all([promise1, promise2])