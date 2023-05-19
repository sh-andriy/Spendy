// text = document.getElementById('rate');
//
// window.onload = function(){
//     getRateEur()
//         .then(rateEur => {
//             getRateUsd()
//                 .then(rateUsd => {
//                     rateEur = roundToTwoDecimal(rateEur);
//                     rateUsd = roundToTwoDecimal(rateUsd);
//                     text.innerText = 'USD:  ' + rateUsd + ' / EUR:  ' + rateEur;
//                 })
//                 .catch(error => console.log('Error:', error));
//         })
//         .catch(error => console.log('Error:', error));
// };
//
// var myHeaders = new Headers();
// myHeaders.append("apikey", "");
//
// var requestOptions = {
//     method: 'GET',
//     redirect: 'follow',
//     headers: myHeaders
// };
//
// function getRateUsd() {
//     return new Promise((resolve, reject) => {
//         fetch("https://api.apilayer.com/exchangerates_data/convert?to=UAH&from=USD&amount=1", requestOptions)
//             .then(response => response.text())
//             .then(result => {
//                 const obj1 = JSON.parse(result);
//                 resolve(obj1.result);
//             })
//             .catch(error => reject(error));
//     });
// }
//
// function getRateEur() {
//     return new Promise((resolve, reject) => {
//         fetch("https://api.apilayer.com/exchangerates_data/convert?to=UAH&from=EUR&amount=1", requestOptions)
//             .then(response => response.text())
//             .then(result => {
//                 const obj2 = JSON.parse(result);
//                 resolve(obj2.result);
//             })
//             .catch(error => reject(error));
//     });
// }
//
// function roundToTwoDecimal(number) {
//     return parseFloat(number).toFixed(2);
// }

// ---------------------------------DEPOSIT-------------------------------------


function percentage(percent, total) {
    return ((total/100)*percent).toFixed(2)
};

function getRange(val){
    const result = parseFloat(val) + parseFloat(percentage(11.5, val));
    document.getElementById("potentialIncome").innerHTML = result;
    document.getElementById("inputNumber").value = val;
};

function cloneValue(val) {
    if(val > 100000){
        val = 100000;
        inputNumber.value = val;
    }else if(val <= 0){
        val = 0;
        inputNumber.value = val;
    }
    document.getElementById("range").value = val;
    const result = parseFloat(val) + parseFloat(percentage(11.5, val));
    document.getElementById("potentialIncome").innerHTML = result.toFixed(2);
};