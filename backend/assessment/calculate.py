def calculate_risk_level(speed, course, altitude, temp, soil_hum, hum, latitude, longitude, fix_quality, num_of_satellites, hdop):
    risk_score = (speed * 0.2) + (course * 0.1) + (temp * 0.15) + (soil_hum * 0.2) + (hum * 0.15) + (altitude * 0.2)
    if risk_score < 50:
        risk_level = "无风险"
    elif risk_score < 80:
        risk_level = "低风险"
    elif risk_score < 90:
        risk_level = "中风险"
    else:
        risk_level = "高风险"
    
    return risk_level, latitude, longitude, fix_quality, num_of_satellites, hdop, altitude, speed, course, temp, hum, soil_hum
