// script.js
document.addEventListener('DOMContentLoaded', function () {
    const loginPage = document.getElementById('loginPage');
    const mainPage = document.getElementById('mainPage');
    const loginForm = document.getElementById('loginForm');
    const weatherInfo = document.getElementById('weatherInfo');
    
    // Check if user is already logged in
    const loggedInUser = localStorage.getItem('loggedInUser');
    if (loggedInUser) {
        showMainPage();
    }

    // Handle login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;
        // Simulating successful login
        localStorage.setItem('loggedInUser', username);
        addUserToJson(username); // Add user to JSON file
        showMainPage();
    });

    // Function to show main page
    function showMainPage() {
        loginPage.style.display = 'none';
        mainPage.style.display = 'block';
        displayWeatherInfo(); // Display weather information
    }

    // Function to display weather information
    function displayWeatherInfo() {
        const apiUrl = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters&key=3878c1b028cb526e5cad1a5830a67bb2&city=110000&correction=n&extensions=base';

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const weather = data.lives[0]; // Get the first item in the array
                weatherInfo.innerHTML = `<h3>当前天气：</h3>
                                          <p>省份：${weather.province}</p>
                                          <p>城市：${weather.city}</p>
                                          <p>天气：${weather.weather}</p>
                                          <p>温度：${weather.temperature_float}℃</p>
                                          <p>风向：${weather.winddirection}</p>
                                          <p>风力：${weather.windpower}</p>
                                          <p>湿度：${weather.humidity_float}%</p>
                                          <p>报告时间：${weather.reporttime}</p>`;
            })
            .catch(error => {
                console.error('Error fetching weather information:', error);
                weatherInfo.innerHTML = '天气预报数据获取失败';
            });
    }
    
// Append the input field and button to the mainPage or an appropriate location in your HTML
mainPage.appendChild(searchInput);
mainPage.appendChild(searchButton);
    // Function to add user to JSON file
    function addUserToJson(username) {
        fetch('users.json')
            .then(response => response.json())
            .then(data => {
                data.users.push(username); // Add new user to the array
                return fetch('users.json', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
            })
            .then(response => {
                if (response.ok) {
                    console.log('New user added to JSON file');
                } else {
                    console.error('Failed to add new user to JSON file');
                }
            })
            .catch(error => {
                console.error('Error adding user to JSON file:', error);
            });
    }
});
