text = document.getElementById('rate');

window.onload = function(){
    getRateEur()
        .then(rateEur => {
            getRateUsd()
                .then(rateUsd => {
                    rateEur = roundToTwoDecimal(rateEur);
                    rateUsd = roundToTwoDecimal(rateUsd);
                    text.innerText = 'USD:  ' + rateUsd + ' / EUR:  ' + rateEur;
                })
                .catch(error => console.log('Error:', error));
        })
        .catch(error => console.log('Error:', error));
};

var myHeaders = new Headers();
myHeaders.append("apikey", "EFVp0pm94mHcEWAnqSIHHldR12YU8Q5R");

var requestOptions = {
    method: 'GET',
    redirect: 'follow',
    headers: myHeaders
};

function getRateUsd() {
    return new Promise((resolve, reject) => {
        fetch("https://api.apilayer.com/exchangerates_data/convert?to=UAH&from=USD&amount=1", requestOptions)
            .then(response => response.text())
            .then(result => {
                const obj1 = JSON.parse(result);
                resolve(obj1.result);
            })
            .catch(error => reject(error));
    });
}
  
function getRateEur() {
    return new Promise((resolve, reject) => {
        fetch("https://api.apilayer.com/exchangerates_data/convert?to=UAH&from=EUR&amount=1", requestOptions)
            .then(response => response.text())
            .then(result => {
                const obj2 = JSON.parse(result);
                resolve(obj2.result);
            })
            .catch(error => reject(error));
    });
}

function roundToTwoDecimal(number) {
    return parseFloat(number).toFixed(2);
}
