// 获取数据并更新页面的函数
async function fetchData() {
    try {
        const response = await fetch('http://10.0.0.212:8080/reading');
        const data = await response.json(); 

        // 检查数据是否包含温度和湿度信息
        if ('temperature' in data && 'humidity' in data) {
            // 更新页面上的数据
            document.getElementById('real-time').innerHTML = `
                <p>Temperature: ${data.temperature}</p>
                <p>Humidity: ${data.humidity}</p>
            `;
        } else {
            console.error('Temperature or humidity data missing in response');
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchData();
setInterval(fetchData, 10000); // 每10秒更新一次
function displayContent(event, pageId) {
    // 阻止链接的默认跳转行为
    event.preventDefault();

    // 隐藏所有内容区域
    var contentDivs = document.getElementsByClassName('content');
    for (var i = 0; i < contentDivs.length; i++) {
        contentDivs[i].classList.remove('active');  // 使用classList方法来移除'active'类
        contentDivs[i].style.display = 'none';
    }

    // 显示所选的内容区域，并添加'active'类
    var activeContent = document.getElementById(pageId);
    activeContent.style.display = 'block';
    activeContent.classList.add('active');

    // 更新导航链接的活动状态
    var navLinks = document.querySelectorAll('nav a');
    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].classList.remove('active');  // 使用classList方法来移除'active'类
    }
    document.querySelector('nav a[href="#' + pageId + '"]').classList.add('active');
}

// 设置日期和星期
var today = new Date();
document.getElementById('date').textContent = today.toLocaleDateString('zh-CN');
document.getElementById('weekday').textContent = today.toLocaleDateString('zh-CN', { weekday: 'long' });

// 为导航链接添加点击事件监听器
var navLinks = document.querySelectorAll('nav a');
navLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
        var pageId = this.getAttribute('href').substring(1);  // 从href中获取页面ID
        displayContent(event, pageId);
    });
});
