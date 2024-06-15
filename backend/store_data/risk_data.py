from utils.db_utils import execute_query

async def store_risk_data(
        timestamp,
        risk_level,
        latitude,
        longitude,
        hdop,
        altitude,
        speed_over_ground,
        course_over_ground,
        soil_humidity,
        risk_score):
    
    query = """
    INSERT INTO landslide_risk_status (
        timestamp,
        risk_level,
        latitude,
        longitude,
        hdop,
        altitude,
        speed_over_ground,
        course_over_ground,
        soil_humidity,
        risk_score
    ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)
    """
    args = (
        timestamp,
        risk_level,
        latitude,
        longitude,
        hdop,
        altitude,
        speed_over_ground,
        course_over_ground,
        soil_humidity,
        risk_score
    )
    try:
        await execute_query(query, args)
    except Exception as e:
        print(f"Failed to store risk data: {str(e)}")

