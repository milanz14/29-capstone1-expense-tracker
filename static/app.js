let ctx = document.getElementById('myChart').getContext('2d')
let container = document.getElementById('myChart')
let loader = document.querySelector('.loader');
const bodyContainer = document.getElementById('table-container');
const userID = document.getElementById('user').innerHTML;
const URL = 'https://budgee-app.herokuapp.com';
// const URL = 'http://localhost:5000';

const showLoadingView = () => {
    loader.innerHTML = '<p>LOADING... </p>'
};

const stopLoadingView = () => {
    loader.innerHTML = ' ';
}

const fetchData = async (e) => {
    e.preventDefault();
    
    await axios.get(`${URL}/api/${userID}/transactions`).then(response => {
        // console.log(response.data.transactions)
        stopLoadingView();
        for (let transaction of response.data.transactions) {
            const location = transaction.location;
            const amount = transaction.amount;
            const category = transaction.category;
            const details = transaction.details;
            const transactionID = transaction.id;
            const newTR = document.createElement('tr')
            
            newTR.innerHTML = `
                <td><a href="${URL}/users/${userID}/transactions/${transactionID}"</a>${location}</td>
                <td>${amount}</td>
                <td>${category}</td>
                <td>${details}</td>`
            
            bodyContainer.append(newTR);
            
        }
    });
};

showLoadingView();
document.addEventListener('DOMContentLoaded', fetchData);
