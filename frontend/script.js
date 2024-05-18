// 获取数据并更新页面的函数
async function fetchData() {
    try {
        // 发送GET请求获取数据
        const response = await fetch('http://10.0.0.212:8080/reading');
        const data = await response.json(); // 解析JSON响应

        // 更新页面上的数据
        document.getElementById('data').innerHTML = `
            <p>Temperature: ${data.temperature}</p>
            <p>Humidity: ${data.humidity}</p>
        `;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


fetchData();
setInterval(fetchData, 10000); // 每10秒更新一次
