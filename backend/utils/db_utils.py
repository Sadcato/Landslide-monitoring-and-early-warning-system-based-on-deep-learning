import aiomysql

async def get_db_connection():
    try:
        conn = await aiomysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='password',
            db='trinity',
            autocommit=True
        )
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {str(e)}")
        return None

async def execute_query(query, args=None):
    conn = await get_db_connection()
    if conn is None:
        return  # Early return if connection is not established

    try:
        cur = await conn.cursor()
        await cur.execute(query, args)
        results = await cur.fetchall()
        await cur.close()
        return results
    except Exception as e:
        print(f"Failed to execute query: {str(e)}")
    finally:
        conn.close()
