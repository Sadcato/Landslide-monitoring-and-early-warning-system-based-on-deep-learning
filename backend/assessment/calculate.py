def calculate_risk_level(data):
    if any(value is None for value in data.values()):
        return "数据不完整", data, 0
    
    # 确保数据存在，即使为0也要参与计算
    speed = float(data['speed']) if data['speed'] is not None else 0
    soil_hum = float(data['soil_hum']) if data['soil_hum'] is not None else 0

    # 计算风险评分
    risk_score = speed + (soil_hum * 0.1)

    if risk_score < 10:
        risk_level = "无风险"
    elif risk_score < 15:
        risk_level = "低风险"
    elif risk_score < 25:
        risk_level = "中风险"
    else:
        risk_level = "高风险"
    
    data['risk_level'] = risk_level
    return risk_level, data, risk_score
