// script.js
document.addEventListener('DOMContentLoaded', function () {
    const loginPage = document.getElementById('loginPage');
    const mainPage = document.getElementById('mainPage');
    const loginForm = document.getElementById('loginForm');
    const weatherInfo = document.getElementById('weatherInfo');
    const cityInput = document.getElementById('cityInput'); // 假设您已经有一个输入框元素
    const searchButton = document.getElementById('searchButton'); // 假设您已经有一个按钮元素

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
        // 这里我们使用北京市作为默认的城市代码进行天气信息的显示
        const defaultAdcode = '110000';
        fetchWeatherByAdcode(defaultAdcode);
    }

    // 修改后的函数，根据adcode获取天气信息
    function fetchWeatherByAdcode(adcode) {
        const apiUrl = `https://restapi.amap.com/v3/weather/weatherInfo?parameters&key=3878c1b028cb526e5cad1a5830a67bb2&city=${adcode}&extension=all`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const weather = data.lives[0];
                weatherInfo.innerHTML = `
                    <h3>当前天气：</h3>
                    <p>省份：${weather.province}</p>
                    <p>城市：${weather.city}</p>
                    <p>天气：${weather.weather}</p>
                    <p>温度：${weather.temperature}℃</p>
                    <p>风向：${weather.winddirection}</p>
                    <p>风力：${weather.windpower}</p>
                    <p>湿度：${weather.humidity}%</p>
                    <p>报告时间：${weather.reporttime}</p>
                `;
            })
            .catch(error => {
                console.error('Error fetching weather information:', error);
                weatherInfo.innerHTML = '天气预报数据获取失败';
            });
    }

    // 增加的函数，根据城市名称查找adcode
    function getAdcodeByCityName(cityName) {
        return fetch('adcode.json')
            .then(response => response.json())
            .then(data => {
                const cityData = data.find(item => item["中文名"] === cityName);
                return cityData ? cityData.adcode : null;
            })
            .catch(error => {
                console.error('Error fetching adcode:', error);
                return null; // 确保在发生错误时返回null
            });
    }

    // 为搜索按钮添加事件处理程序
    searchButton.addEventListener('click', function() {
        const cityName = cityInput.value; // 获取用户输入的城市名称
        getAdcodeByCityName(cityName).then(adcode => {
            if (adcode) {
                fetchWeatherByAdcode(adcode); // 使用获取到的adcode调用天气信息函数
            } else {
                weatherInfo.innerHTML = '未找到对应的城市代码';
            }
        });
    });
});

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

