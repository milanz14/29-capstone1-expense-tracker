const getButton = document.getElementById('get-btn')
const bodyContainer = document.getElementById('table-container')
const userID = document.getElementById('user').innerHTML
// const URL = 'https://budgee-app.herokuapp.com'
const URL = 'http://localhost:5000'

const fetchData = async (e) => {
    e.preventDefault();
    
    await axios.get(`${URL}/api/${userID}/transactions`).then(response => {
        console.log(response.data.transactions)
        for (let transaction of response.data.transactions) {
            const location = transaction.location;
            const amount = transaction.amount;
            const date = transaction.date;
            const category = transaction.category;
            const details = transaction.details;
            const transactionID = transaction.id;
            const newTR = document.createElement('tr')
            
            newTR.innerHTML = `
                <td><a href="${URL}/users/${userID}/transactions/${transactionID}"</a>${location}</td>
                <td>${amount}</td>
                <td>${category}</td>
                <td>${date}</td>
                <td>${details}</td>`
            
            bodyContainer.append(newTR);
            
        }
    });
};

document.addEventListener('DOMContentLoaded', fetchData);
