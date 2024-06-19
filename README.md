# Landslide-monitoring-and-early-warning-system-based-on-deep-learning  
#山体滑坡的监测和预警系统
#该项目搭建于龙芯教育派开发板，Python为后端语言，FastAPI为架构使用sse协议作api通信前端 
#项目将传感器集成到一块开发板mcu为ATmega328p，将数据打包处理再走串口传输到开发板上
#mcu:ATmega328p  
#sensor:LC760Z(GPS);DH11;YL-69soil moisture sensor  
#demo board:ls2k1000(龙芯教育派)  

#developer log  
#2024/5/18 After uploading to the backend, the frontend can feed back the most basic json  

#2024/5/25 Complete the homemade arduino development board and connect the LC760Z, DHT11 and soil moisture sensor to complete the serial port transmission  
#2024/6/5 After a week of rest, I finally started this project again. Now it can perfectly push data to the front end and you can see its real-time data on the front-end web page, and it has improved the logic handling of data transmission errors  
![image](https://github.com/Sadcato/Landslide-monitoring-and-early-warning-system-based-on-deep-learning/blob/main/img/WechatIMG1.jpg)  
![image](https://github.com/Sadcato/Landslide-monitoring-and-early-warning-system-based-on-deep-learning/blob/main/img/read.jpg)


