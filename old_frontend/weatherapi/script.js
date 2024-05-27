


document.addEventListener('DOMContentLoaded', function () {
    const loginPage = document.getElementById('loginPage');
    const mainPage = document.getElementById('mainPage');
    const loginForm = document.getElementById('loginForm');
    const weatherInfo = document.getElementById('weatherInfo');
    const cityInput = document.getElementById('cityInput'); 
    const searchButton = document.getElementById('searchButton'); 

    // Check if the user is logged in
    const loggedInUser = localStorage.getItem('loggedInUser');
    if (loggedInUser) {
        showMainPage();
    }

    // Handle login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const username = loginForm.username.value;
        const password = loginForm.password.value;
        // Simulate successful login
        localStorage.setItem('loggedInUser', username);
        addUserToJson(username); // Add users to JSON file
        showMainPage();
    });

    // mainpage
    function showMainPage() {
        loginPage.style.display = 'none';
        mainPage.style.display = 'block';
        displayWeatherInfo(); // Default weather information for Beijing
    }

    
    function displayWeatherInfo() {
        const defaultCityCode = '110000'; 
        fetchWeatherByCityCode(defaultCityCode);
    }

    // get weather information based on city code
    function fetchWeatherByCityCode(cityCode) {
        const apiUrl = `https://restapi.amap.com/v3/weather/weatherInfo?parameters&key=3878c1b028cb526e5cad1a5830a67bb2&city=${cityCode}&extension=all`;

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

    searchButton.addEventListener('click', function() {
        const cityName = cityInput.value.trim(); // 获取用户输入的城市名称并去除空格
        if (!cityName) {
            weatherInfo.innerHTML = '请输入城市名称';
            return;
        }
    
        // 确保ad.json文件路径正确
        fetch('ad.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应错误');
                }
                return response.json();
            })
            .then(data => {
                const cityData = data.find(item => item["中文名"] === cityName);
                if (cityData) {
                    fetchWeatherByCityCode(cityData.adcode); // 使用找到的城市代码获取天气信息
                } else {
                    weatherInfo.innerHTML = '未找到对应的城市代码';
                }
            })
            .catch(error => {
                console.error('Error fetching city code:', error);
                weatherInfo.innerHTML = '获取城市代码时发生错误';
            });
    });
    // 将用户添加到JSON文件
    function addUserToJson(username) {
        // 操操操草草草草草草草草草草草草草草草草草草草草操
    }
});