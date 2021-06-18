let ctx = document.getElementById('myChart').getContext('2d')
let container = document.getElementById('myChart')
let loader = document.querySelector('.loader');
const bodyContainer = document.getElementById('table-container');
const userID = document.getElementById('user').innerHTML;
const URL = 'https://budgee-app.herokuapp.com';
// const URL = 'http://localhost:5000';

let labels = [];
let amounts = [];
let backgroundColors = [];

const showLoadingView = () => {
    loader.innerHTML = '<p>LOADING... </p>'
};

const stopLoadingView = () => {
    loader.innerHTML = ' ';
}
showLoadingView();

const randomColors = () => {
    let r = Math.floor(Math.random() * 255) + 1;
    let g = Math.floor(Math.random() * 255) + 1;
    let b = Math.floor(Math.random() * 255) + 1;
    color = `rgb(${r}, ${g}, ${b})`
    return color;
};

const fetchData = async (e) => {
    e.preventDefault();
    
    await axios.get(`${URL}/api/${userID}/transactions`).then(response => {
        // console.log(response.data.transactions)
        stopLoadingView();
        for (let transaction of response.data.transactions) {
            const location = transaction.location;
            labels.push(location)
            const amount = transaction.amount;
            amounts.push(amount)
            backgroundColors.push(randomColors());
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

const generateChart = () => {
    const data = {
        labels: labels,
        datasets: [{
            label: 'Your Spending',
            backgroundColor: backgroundColors,
            data: amounts,
            hoverOffset: 4
        }],
    };

    const config = {
        type: 'doughnut',
        data: data,
        options: {
            legend: {
                display: true,
                position: 'bottom',
            },
        },
    };

    let myChart = new Chart(
        ctx,
        config
    );

    myChart.canvas.parentNode.style.height = '550px';
    myChart.canvas.parentNode.style.width = '550px';
}

document.addEventListener('DOMContentLoaded', fetchData);
document.addEventListener('DOMContentLoaded', generateChart);